from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser, Plant, Review


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'
            field.label_tag(attrs={'style': 'color: #00563FFF;'})

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role')

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'c'
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'


class EditPlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields=['name', 'scientific_name', 'origin', 'age', 'description','care_instructions', 'image']
        widgets = {'category': forms.Select(attrs={'class': 'form-control'}), 'image': forms.FileInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(11)]  # Choices from 0 to 10

    rating = forms.ChoiceField(label='Rating', choices=RATING_CHOICES)

    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control mb-3'

    def clean_rating(self):
        rating = int(self.cleaned_data.get('rating'))
        if rating < 0 or rating > 10:
            raise forms.ValidationError("Rating must be between 0 and 10.")
        return rating


class SearchForm(forms.Form):
    query = forms.CharField()

