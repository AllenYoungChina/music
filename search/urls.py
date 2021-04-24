from django.urls import path

from .views import search

urlpatterns = [
    path('<int:page>.html', search, name='search'),
]
