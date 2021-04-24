from django.urls import path

from .views import comment

urlpatterns = [
    path('<int:id>.html', comment, name='comment'),
]