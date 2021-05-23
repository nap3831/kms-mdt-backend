from django.contrib import admin
from django.urls import path, include
from .models import Blog, BlogCategory, Comment

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    def has_add_permission(self, request, obj=None):
        return False
    list_display = ['title', 'sub_title', 'cover','own_user', 'category']
    list_filter = ['own_user', 'category']
    ordering = ('id',)
    
admin.site.register(Blog, BlogAdmin)


class BlogCategoryAdmin(admin.ModelAdmin):
    model = BlogCategory
    ordering = ('id',)
    


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'cate_image', 'category_image']
    readonly_fields = ('category_image',)
    change_form_template="admin/blog/upload-category-images.html"


admin.site.register(BlogCategory, TemplateAdmin)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    def has_add_permission(self, request, obj=None):
        return True

    list_display = ['published', 'content', 'user_comment']
    ordering = ('id',)
    
admin.site.register(Comment, CommentAdmin)
