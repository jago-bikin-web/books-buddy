from django.urls import path
from main.views import *


app_name = 'main'


urlpatterns = [
    path('', show_landing_page, name='landing_page'),
    path('signup/', signup, name='signup'),
]