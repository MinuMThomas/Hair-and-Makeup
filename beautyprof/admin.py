from django.contrib import admin
from .models import Profile
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio')
