from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Profile


class ProfileListView(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
