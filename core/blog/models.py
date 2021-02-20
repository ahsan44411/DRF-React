from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    
    # Model Manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    # CharField
    title = models.CharField(max_length=250, null=True, blank=True)

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(
        max_length=10, choices=options, default='published')

    # TextField
    excerpt = models.TextField(null=True)
    content = models.TextField()

    # Slug
    slug = models.SlugField(max_length=250, unique_for_date="published")

    # DateTime
    published = models.DateTimeField(default=timezone.now)

    # Relations
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")

    objects = models.Manager()
    postobjects = PostObjects()
    
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title+' -- '+self.author
