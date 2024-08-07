from django.urls import path
from .views import check_enclosure, enclosure_list, clear_enclosures

urlpatterns = [
    path('check/', check_enclosure, name='check_enclosure'),
    path('clear/', clear_enclosures, name='clear_enclosures'),
    path('list/', enclosure_list, name='enclosure_list'),
]