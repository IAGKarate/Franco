from django.contrib import admin
from .models import Post, Comment



Post.objects.order_by('created_date')
admin.site.register(Post)
admin.site.register(Comment)

# Register your models here.
