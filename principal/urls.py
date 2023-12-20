from django.urls import path
from django.contrib import admin

from principal.views import load_data, home, load_recommendations, login_petition

# Add your URLs here.

urlpatterns = [
    path('login/', login_petition, name='login'),
    path('home/', home, name='home'),
    path('load_db/', load_data, name='load_db'),
    path('load_recommendations/', load_recommendations, name='load_recommendations')
]