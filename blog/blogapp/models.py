from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length = 100)
    objects = models.Manager()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length = 100)
    objects = models.Manager()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    
    title = models.CharField(max_length=100)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)
    objects = models.Manager()

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['modified_time', '-created_time']

    def increase_views(self):
        self.views += 1 
        self.save(update_fields=['views'])