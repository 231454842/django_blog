from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """docstring fo PostAdmin."""
    list_display=['title','create_time','modified_time','Category','author']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
