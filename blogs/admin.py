from django.contrib import admin
from .models import Blog
from .models import Post
from .models import Comment

class PostInline(admin.StackedInline):
    model = Post
    extra = 2

	
class BlogAdmin(admin.ModelAdmin):
	inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('id','title', 'date','blog_id')	
    list_filter = ['date']
    fieldsets=[
            (None,{'fields': ['blog']}),
            ('content information',{'fields': ['title','summary','text']}),
            ('Date information', {'fields': ['date']}),
    ]
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date','post_id')	
    search_fields = ['text']
    list_filter = ['date']
    fieldsets = [
		(None,{'fields': ['post']}),
        ('content',               {'fields': ['text']}),
        ('Date information', {'fields': ['date']}),
    ]

admin.site.register(Blog,BlogAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
