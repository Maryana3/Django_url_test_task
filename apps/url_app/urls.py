
# urls.py
from django.urls import path
from .views import MyView

urlpatterns = [

    path('home/', MyView.as_view(), name='home'),
]
