from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# from django.views import ListView, View
from .models import Profile
from .forms import ProfileForm


# class ProfileListView(ListView):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')

class ProfileListView(generic.ListView):
    model = Profile
    queryset = Profile.objects.order_by('created')
    template_name = "index.html"
    paginate_by = 6


class  ProfileDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.order_by('updated')
        profile = get_object_or_404(queryset, slug=slug)
        reviews = profile.reviews.filter(approved=True).order_by('created_on')

        return render(
            request,
            "prof_detail.html",
            {
                "profile": profile,
                "profile_form": ProfileForm,
            })
