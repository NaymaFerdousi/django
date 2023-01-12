from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='h'),
    path('del/<int:id>',views.rem,name='rem'),
]