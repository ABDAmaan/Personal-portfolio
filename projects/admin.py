from django.contrib import admin
from .models import Post, Project, Tags, Tools, PostImage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tags)
admin.site.register(Tools)
admin.site.register(Post, PostAdmin)
admin.site.register(Project, PostAdmin)
admin.site.register(PostImage)
