from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('for_home <int:for_home>', views.index, name='for_home'),
    path('food_for_kids <int:food_for_kids>',
         views.index, name='food_for_kids'),
]
