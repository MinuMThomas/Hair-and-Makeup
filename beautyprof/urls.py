from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileListView.as_view(), name='home'),
    path('add/', views.add_profile, name='add_profile'),
    path('view/', views.view_my_profile, name='view_my_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile_detail'),
] 
