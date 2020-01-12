from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Meals, Category


# Apply summernote to all TextField in model.
class MealsModelAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = [
        'name',
        'preparation_time',
        'price',
        'people'
    ]
    search_fields = [
        'name',
        'description',
    ]
    list_filter = (
        'category',
        'people',
    )


admin.site.register(Meals, MealsModelAdmin)
admin.site.register(Category)
