from django.contrib import admin
from webapp.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'category', 'created_at']
    list_filter = ['author', 'category']
    list_display_links = ['pk', 'title']
    search_fields = ['title', 'text']
    fields = ['title', 'author', 'text', 'category', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)