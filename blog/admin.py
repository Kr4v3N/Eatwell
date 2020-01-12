from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post, Category, Comment


# Apply summernote to all TextField in model.
class PostModelAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = [
        'title',
        'author',
        'category',
        'created'
    ]
    search_fields = [
        'title',
        'content',
    ]
    list_filter = (
        'category',
        'tags',
        'created'
    )



admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)
