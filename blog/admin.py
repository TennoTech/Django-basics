from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

admin.site.register(models.Category)


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {
        'slug': ("title", ),
    }


# @admin.register(models.Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('post', 'name', 'publish', 'status')
#     list_filter = ('status', 'publish')
#     search_fields = ('name', 'email', 'content')

admin.site.register(models.Comment, MPTTModelAdmin)

