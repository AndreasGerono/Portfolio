from django.shortcuts import render


def index(request):
    context = {
        "articles": range(5),
    }
    return render(request, 'index.html', context)


def article_detail(request, year, month, slug):
    print(year, month, slug)
    context = {
        "article": 'article',
    }
    return render(request, 'article.html', context)


def month_archive(request, year, month):
    print(year, month)
    context = {
        "articles": range(2),
    }
    return render(request, 'archive.html', context)


def year_archive(request, year):
    print(year)
    context = {
        "articles": range(10),
    }
    return render(request, 'archive.html', context)
