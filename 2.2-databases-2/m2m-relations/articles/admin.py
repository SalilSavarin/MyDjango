from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ArticleScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                is_main_count += 1
                if is_main_count > 1:
                    raise ValidationError('Основной тег может быть только один')
            if is_main_count == 0:
                raise ValidationError('Обязательно нужен основной тег')
        return super().clean()

class ArticleScopeInLine(admin.TabularInline):
    model = Scope
    formset = ArticleScopeInLineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInLine]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
