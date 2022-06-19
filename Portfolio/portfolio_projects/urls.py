from django.urls import path
from portfolio_projects import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('archive', views.archive, name="archive"),
    path('demo/<int:id>', views.demo, name="demo"),
    path('<int:year>', views.year_archive, name='year_archive'),
    path('<int:year>/<int:month>', views.month_archive, name='month_archive'),
    path('<int:year>/<int:month>/<slug:slug>', views.article_detail, name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.my404
