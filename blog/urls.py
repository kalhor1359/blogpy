from django.urls import path
from . import views

urlpatterns = [
      path('',views.Indexpage.as_view(), name='index')


]