from django import forms
from .models import Profile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name', 'profession', 'email', 'avatar', 'bio']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profession', 'email', 'avatar', 'bio']
        widgets = {
            'content': SummernoteWidget(),
                    }