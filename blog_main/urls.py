from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('catfilter/<int:id>/',categoryFilter,name='catfilter'),
    path('continue_reading/<slug:slug>/',Continue_Reading,name='continue_reading'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
]