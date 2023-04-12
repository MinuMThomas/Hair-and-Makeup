from django.urls import path
from beautyprof.views import ProfileListView

urlpatterns = [
    path('', ProfileListView.as_view(), name='home'),
]
