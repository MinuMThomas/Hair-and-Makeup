from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class ProfileListView(generic.ListView):
    model = Profile
    queryset = Profile.objects.order_by('created')
    template_name = "index.html"
    paginate_by = 6


class ProfileDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            "profile_detail.html",
            {
                "profile": profile,
            })


@login_required
def view_my_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    # add condition if profile dosent exist readirect to do create profile
    return render(request, 'view_profile.html', {'profile': profile})


# class AddProfile(SuccessMessageMixin, LoginRequiredMixin, CreateView):
#     model = Profile
#     template_name = 'add_profile.html'
#     success_url = reverse_lazy('home')
#     form_class = ProfileForm
#     success_message = 'created profile'

#     def form_valid(self, form):
#         if self.request.POST.get('status'):
#             form.instance.status = int(self.request.POST.get('status'))
#         form.instance.author = self.request.user
#         return super().form_valid(form)


@login_required
def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
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
        form = ProfileForm(request.POST, instance=profile)
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
