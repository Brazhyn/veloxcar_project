from django.urls import path, include
from . import views

category_patterns = [
    path('', views.categories_list),
    path('<str:category_name>/', views.categories_list), 
    path('<str:category_name>/create_post/', views.create_post),
    path('<str:category_name>/<slug:post_slug>/', views.post_detail),
    path('<str:category_name>/<slug:post_slug>/update/', views.update_post),
    path('<str:category_name>/<slug:post_slug>/delete/', views.delete_post)
]


urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post),
    path('categories/', include(category_patterns))
]
