from django.contrib import admin
from .models import Profile
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_filter = ('name', 'created')
    summernote_fields = ('bio')
    list_display = ('name', 'profession')
    search_fields = ['profession']
