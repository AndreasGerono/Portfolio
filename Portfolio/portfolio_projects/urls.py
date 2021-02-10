from django.urls import path
from portfolio_projects import views

urlpatterns = [
    path('', views.index, name="Welcome"),
    path('<int:year>/', views.year_archive, name='year_archive'),
    path('<int:year>/<int:month>/', views.month_archive, name='month_archive'),
    path('<int:year>/<int:month>/<slug:slug>/', views.article_detail, name='article'),
]
