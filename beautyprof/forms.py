from django import forms
from .models import Profile, Review


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profession', 'email', 'county', 'avatar', 'bio']
        prepopulated_fields = {'slug': 'user'}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)
