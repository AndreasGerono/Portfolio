from django.contrib import admin
from portfolio_projects import models as m

# Register your models here.


@admin.register(m.Article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'date')
    ordering = ('-date',)
    readonly_fields = ('slug',)
