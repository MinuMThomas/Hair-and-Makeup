from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileListView.as_view(), name='home'),
     path('<slug:slug>/', views.ProfileDetail.as_view(), name='prof_detail'),
]
