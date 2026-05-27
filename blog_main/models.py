from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    Category_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Category_name  

STATUS_CHOISE = (
    ('Draft','Draft'),
    ('Published','Published')
)

class Blog(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    blog_body = models.TextField(max_length=2000)
    short_description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOISE,default='Draft')
    featured_image = models.ImageField(upload_to='upload/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title