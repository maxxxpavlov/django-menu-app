
from django import template
from django.template import loader, Context
from menu.tree import getMenuTree

register = template.Library()


@register.simple_tag
def draw_menu(menuName, selectedElementId):
    menu = loader.get_template('menu.html')
    tree = getMenuTree(menuName, selectedElementId)
    return menu.render({'tree': tree, 'menuName': menuName})
