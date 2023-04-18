from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileListView.as_view(), name='home'),
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('add/', views.add_profile, name='add_profile'),
    path('edit/<slug:slug>', views.edit_profile, name='edit_profile'),
    path('view/<slug:slug>', views.view_my_profile, name='view_my_profile'),
    path('delete/<slug:slug>', views.delete_profile, name='delete_profile'),
]
