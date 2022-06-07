from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'datepublish', 'status')
    list_filter = ('status', 'datepublish', 'date_created', 'author',)
    search_fields = ('title', 'body'),
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'datepublish' 
    ordering = ('status', 'datepublish')