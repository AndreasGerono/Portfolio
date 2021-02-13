from django.urls import path
from portfolio_projects import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('article', views.archive, name="article"),
    path('<int:year>/', views.year_archive, name='year_archive'),
    path('<int:year>/<int:month>/', views.month_archive, name='month_archive'),
    path('<int:year>/<int:month>/<slug:slug>/', views.article_detail, name='article'),
]


handler404 = views.my404
