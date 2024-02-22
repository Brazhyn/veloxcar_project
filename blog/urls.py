from django.urls import path, include
from . import views

app_name = 'blog'

category_patterns = [
    path('<slug:category_slug>/', views.category_posts_list, name='category_posts_list'),
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/<slug:post_slug>/update/', views.UpdatePostView.as_view(), name='update_post'),
    path('<slug:category_slug>/<slug:post_slug>/delete/', views.DeletePostView.as_view(), name='delete_post')
]


urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('categories/', include(category_patterns)),
    path('about_us/', views.about_us, name='about_us'),
    path('all_posts/', views.all_posts, name='all_posts')
]
