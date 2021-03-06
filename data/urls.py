from django.urls import path
from data import views

from typing import List

app_name: str = 'data'

urlpatterns: List[path] = [
    path('get/', views.CricketDataRetrieveAPI.as_view(), name='get'),
]
