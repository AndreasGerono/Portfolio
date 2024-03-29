from xml.dom.minidom import Document
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, TemplateDoesNotExist, loader
from portfolio_projects import models as m


def index(request):
    articles = m.Article.objects.filter(is_draft=False)[:8]
    context = {
        "articles": articles,
    }
    return render(request, 'index.html', context)

def demo(request, id):
    try:
        t = loader.get_template(f'demo_{id}.html').template
        context = Context()
        return HttpResponse(t.render(context))
    except TemplateDoesNotExist:
        raise Http404


def article_detail(request, year, month, slug):
    article = get_object_or_404(m.Article, date__year=year, date__month=month, slug=slug)  # noqa: E501
    images = article.image_set.all()
    context = {
        "article": article,
        "images": images
    }
    return render(request, 'article.html', context)


def month_archive(request, year, month):
    articles = m.Article.objects.filter(date__year=year, date__month=month, is_draft=False)
    context = {
        "articles": articles,
    }
    return render(request, 'index.html', context)


def year_archive(request, year):
    articles = m.Article.objects.filter(date__year=year, is_draft=False)
    context = {
        "articles": articles,
        }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def my404(request, exception):
    return render(request, '404.html')


def archive(request):
    years = m.Article.objects.values_list('date__year', flat=True).distinct().order_by()

    articles_in_years = []
    for year in sorted(years, reverse=True):
        article = m.Article.objects.filter(date__year=year, is_draft=False)
        articles_in_years.append(article)

    context = {
        "articles_in_years": articles_in_years,
    }

    return render(request, 'archive.html', context)
