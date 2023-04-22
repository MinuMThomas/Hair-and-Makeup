from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import Profile, Review
from .forms import ProfileForm, ReviewForm
from django.contrib.messages.views import SuccessMessageMixin


class ProfileListView(generic.ListView):
    model = Profile
    queryset = Profile.objects.order_by('created')
    template_name = "index.html"
    paginate_by = 6


"""Detailed view of individual Profile"""


class ProfileDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.order_by('updated')
        profile = get_object_or_404(queryset, slug=slug)
        reviews = profile.reviews.order_by("-created_on")
        review_form = ReviewForm()

        return render(
            request,
            "profile_detail.html",
            {
                "profile": profile,
                "reviews": reviews,
                "reviewed": False,
                "review_form": review_form,
                })

    def post(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, slug=slug)
        reviews = profile.reviews.order_by("-created_on")
        review_form = ReviewForm()
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.first_name = request.user.username
            review = review_form.save(commit=False)
            review.profile = profile
            review.save()
            review_form = ReviewForm()
            messages.success(request, 'Review added successfully.')
        else:
            review_form = ReviewForm()

        return render(
            request,
            "profile_detail.html",
            {
                "profile": profile,
                "reviews": reviews,
                "reviewed": True,
                "review_form": review_form,
                })


@login_required
def view_my_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    reviews = profile.reviews.order_by("-created_on")
    return render(request, 'view_profile.html', {'profile': profile,
                                                 'reviews': reviews, })


@login_required
def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            profile = form.save(commit=False)
            profile.save()
            messages.success(request, 'Profile created successfully.')
            return redirect('view_my_profile')
    else:
        form = ProfileForm()
    context = {
        'form': form,
         }

    return render(request, 'add_profile.html', context)


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('view_my_profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'user': profile,
            }
    return render(request, 'edit_profile.html', context)


@login_required
def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully.')
        return redirect('home')
    return render(request, 'delete_profile.html', {'profile': profile})


"""custom error handling page 404 and 500"""


def handler404(request, exception):
    return render(request, "errors/404.html", status=404)


def handler500(request):
    return render(request, "errors/500.html", status=500)
