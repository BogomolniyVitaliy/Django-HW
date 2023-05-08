from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        forms = tuple(filter(lambda form: form.cleaned_data.get('is_main'), self.forms))
        if not forms:
            raise ValidationError('Нужно задать один основной тег')
        if len(forms) > 1:
            raise ValidationError('Основной тэг может быть только один')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    verbose_name = 'Тэг'
    verbose_name_plural = 'Тематика статьи'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    ordering = ('-published_at',)
    inlines = (ScopeInline,)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
