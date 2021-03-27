from django.shortcuts import render, get_object_or_404
from portfolio_projects import models as m


def index(request):
    articles = m.Article.objects.all()[:8]
    context = {
        "articles": articles,
    }
    return render(request, 'index.html', context)


def article_detail(request, year, month, slug):
    article = get_object_or_404(m.Article, date__year=year, date__month=month, slug=slug)  # noqa: E501
    images = article.image_set.all()
    context = {
        "article": article,
        "images": images
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
    years = m.Article.objects.values_list('date__year', flat=True).distinct().order_by()  # noqa: E501
    articles_in_years = []
    for year in sorted(years, reverse=True):
        article = m.Article.objects.filter(date__year=year)
        articles_in_years.append(article)

    context = {
        "articles_in_years": articles_in_years,
    }

    return render(request, 'archive.html', context)
