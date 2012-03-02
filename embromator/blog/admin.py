from blog.models import Post, Author, Comment, Tag
from django.contrib import admin

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tag)