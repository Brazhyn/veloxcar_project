from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False,
                            null=True, unique=True)
    image = models.ImageField(upload_to='blog/admin_images',
                              default='default/no_image.jpg', blank=True, null=True)
    description = models.TextField(
        validators=[MinLengthValidator(20)], blank=False, null=True)
    
    slug = models.SlugField(unique=True, db_index=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return f"{self.name}"


class CarPost(models.Model):
    brand = models.CharField(max_length=150, blank=False)
    car_model = models.CharField(max_length=150, blank=False)
    year = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField(validators=[MinValueValidator(0)])
    excerpt = models.CharField(
        max_length=200, blank=True, default='Немає короткого опису')
    image = models.ImageField(
        upload_to='blog/user_images', default='default/no_image.jpg', blank=False)
    slug = models.SlugField(unique=True, db_index=True)
    date_published = models.DateTimeField(default=timezone.now)
    content = models.TextField(validators=[MinLengthValidator(10)])
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(
        get_user_model(), default=1, on_delete=models.SET_DEFAULT)

    def save(self, *args, **kwargs):
        combined_value = f"{self.brand} {self.car_model} {self.year}"
        base_slug = slugify(combined_value)
        self.slug = base_slug

        if CarPost.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            counter = 1
            while CarPost.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.category.slug, self.slug])

    def __str__(self) -> str:
        return f"{self.brand}, {self.author}"
