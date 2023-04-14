from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# from django.views import ListView, View
from .models import Profile


# class ProfileListView(ListView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')

class ProfileListView(generic.ListView):
    model = Profile
    queryset = Profile.objects.order_by('created')
    template_name = "index.html"
    paginate_by = 6
