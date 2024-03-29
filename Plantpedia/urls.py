"""
URL configuration for Plantpedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from plantpediaApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', user_login),
    path('register/', register_customer),
    path('logout/', logout_view, name='logout'),
    path('plants/', all_plants),
    path('add-plant/', add_plant, name='add_plant'),
    path('plants/<int:plant_id>/', details, name="details")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
