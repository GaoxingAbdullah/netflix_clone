from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profiles/', views.ProfileListView.as_view(), name='profiles'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profile-create'),
    path('watch/<str:profile_id>', views.Watch.as_view(), name='watch'),
]
