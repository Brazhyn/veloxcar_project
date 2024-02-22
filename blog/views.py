from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import CarPostForm, CarPostUpdateForn
from . models import Category, CarPost


def all_posts(request):
    return render(request, 'blog/all_posts.html')

def about_us(request):
    return render(request, 'blog/about_us.html')

def index(request):
    categories = Category.objects.all()
    posts = CarPost.objects.all().order_by('-date_published')[:3]
    return render(request, "blog/index.html", {
        'categories': categories,
        'posts': posts
    })


def category_posts_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = CarPost.objects.filter(category__name=category.name)
    posts_count = posts.count()
    return render(request, 'blog/category_posts_list.html', {
        'posts': posts,
        'category': category,
        'posts_count': posts_count
    })


def post_detail(request, category_slug, post_slug):
    post = get_object_or_404(CarPost, slug=post_slug)
    return render(request, 'blog/post_detail.html', {'post': post})


@method_decorator(login_required, name='dispatch')
class CreatePostView(View):

    def get(self,  request):
        form = CarPostForm()
        return render(request, 'blog/create_update_post.html', {'form': form})

    def post(self, request):
        form = CarPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:index')

        return render(request, 'blog/create_update_post.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UpdatePostView(View):
    
    def get(self, request, category_slug, post_slug):
        post = CarPost.objects.get(slug=post_slug)
        form = CarPostUpdateForn(instance=post)
        return render(request, 'blog/create_update_post.html', {'form': form})
    
    def post(self, request, category_slug, post_slug):
        post = CarPost.objects.get(slug=post_slug)
        form = CarPostUpdateForn(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            category_posts_url = reverse('blog:category_posts_list', kwargs={'category_slug': category_slug})
            return redirect(category_posts_url)
        
        return render(request, 'blog/create_update_post.html', {'form': form})
            

@method_decorator(login_required, name='dispatch')
class DeletePostView(View):
    
    def get(self, request, category_slug, post_slug):
        post = CarPost.objects.get(slug=post_slug)
        return render(request, 'blog/delete_post.html', {'post': post})
    
    def post(self, request, category_slug, post_slug):
        post = CarPost.objects.get(slug=post_slug)
        post.delete()
        category_posts_url = reverse('blog:category_posts_list', kwargs={'category_slug': category_slug})
        return redirect(category_posts_url)

        
        
        
        
