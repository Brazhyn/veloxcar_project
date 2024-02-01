from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Головна сторінка")


def categories_list(request):
    return HttpResponse("Усі категорії")


def create_post(request, category_name=None):
    if category_name is None:
        return HttpResponse("Додавання поста з index")
    else:
        return HttpResponse("Додавання поста з category")


def category_posts_list(request, category_name="якасьназва"):
    return HttpResponse("Список постів в певній катгорії")


def post_detail(request, category_name="якасьназва", post_slug=1):
    return HttpResponse("Детально про певний пост")


def update_post(request, category_name="якасьназва", post_slug=1):
    return HttpResponse("Оновлення поста")


def delete_post(request, category_name="якасьназва", post_slug=1):
    return HttpResponse("видалення поста")


