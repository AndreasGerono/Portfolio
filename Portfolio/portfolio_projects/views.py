from django.shortcuts import render, get_object_or_404
from django.db.models.query import QuerySet
from portfolio_projects import models as m


def index(request):
    articles = m.Article.objects.all()[:5]
    context = {
        "articles": articles,
    }
    return render(request, 'index.html', context)


def article_detail(request, year, month, slug):
    article = get_object_or_404(m.Article, date__year=year, date__month=month, slug=slug)
    context = {
        "article": article,
    }
    return render(request, 'article.html', context)


def month_archive(request, year, month):
    articles = m.Article.objects.filter(date__year=year, date__month=month)
    context = {
        "articles": articles,
    }
    return render(request, 'index.html', context)


def year_archive(request, year):
    articles = m.Article.objects.filter(date__year=year)
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
    for year in years:
        article = m.Article.objects.filter(date__year=year)
        articles_in_years.append(article)

    print(articles_in_years)

    context = {
        "articles_in_years": articles_in_years,
    }

    return render(request, 'archive.html', context)
