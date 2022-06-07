from secrets import choice
from telnetlib import STATUS
from turtle import title
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
        self).get_queryset()\
        .filter(status='published')


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()



    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, blank=True, unique_for_date='datepublish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField(max_length=5000, null=False, blank=False)
    datepublish = models.DateTimeField(default=timezone.now, verbose_name='datepublish')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='date_created')
    dateupdated = models.DateTimeField(auto_now=True, verbose_name='dateupdated')
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='draft')



    def get_abosule_url(self):
        return reverse('blog:post_detail',
            args=[self.datepublish.year,
                  self.datepublish.strftime('%m'),
                  self.datepublish.strftime('%d'),
                  self.slug])

    class Meta:
        ordering = ('-datepublish'),


    def __str__(self):
        return self.title






