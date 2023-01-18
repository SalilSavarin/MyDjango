from django.contrib import admin

from .models import Article, Scope, Tag


class ArticleScopeInLine(admin.TabularInline):
    model = Scope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInLine]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
