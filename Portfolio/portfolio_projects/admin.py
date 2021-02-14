from django.contrib import admin
from portfolio_projects import models as m

# Register your models here.


@admin.register(m.Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'date')
    ordering = ('-date',)
    readonly_fields = ('slug',)
    def get_form(self, request, obj=None, **kwargs):
        form = super(Article, self).get_form(request, obj, **kwargs)
        form.base_fields['text'].widget.attrs['style'] = 'height: 1000px;'
        return form


@admin.register(m.Image)
class Image(admin.ModelAdmin):
    list_display = ('tag',)
