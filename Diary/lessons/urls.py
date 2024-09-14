from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home')),
    path('home/', views.home, name='home'),
    path('lesson/<int:id>/', views.lesson, name='lesson'),
]