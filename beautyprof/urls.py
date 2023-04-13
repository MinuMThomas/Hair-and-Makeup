from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileListView.as_view(), name='home'),
]
