from django.urls import path
from backendApp import views

urlpatterns = [
    path('',views.indexpage,name="index")
]