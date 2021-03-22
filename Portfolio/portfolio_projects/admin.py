from django.contrib import admin
from django.utils.html import format_html
from portfolio_projects import models as m

# Register your models here.


@admin.register(m.Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'date')
    ordering = ('-date',)
    readonly_fields = ('slug',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(Article, self).get_form(request, obj, **kwargs)
        form.base_fields['text'].widget.attrs['style'] = 'height: 800px; font-size: 1.5em;'  # noqa: E501
        return form


@admin.register(m.Image)
class Image(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img style="height: 70px;" src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Preview'
    list_display = ('image_tag', 'image')
    fields = ('article', 'alt', 'image')
