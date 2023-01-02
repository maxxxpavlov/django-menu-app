from django.shortcuts import render, HttpResponse
from menu.tree import getMenuTree
from django.template import loader, Context
# Create your views here.


def index(request, for_home=None, food_for_kids=None):
    indexTemplate = loader.get_template('index.html')
    return HttpResponse(indexTemplate.render({'selectedHomeElementId': for_home, 'selectedFoodElementId': food_for_kids}))
