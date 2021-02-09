from django.urls import path
from portfolio_projects import views

urlpatterns = [
    path('', views.index, name="Welcome"),
]
