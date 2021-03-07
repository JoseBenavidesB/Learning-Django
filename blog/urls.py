from django.urls import path
from . import views

urlpatterns = [
    path('articulos/', views.list, name='list'),
    path('categoria/<int:category_id>', views.category, name="category_from_url_blog"),
    path('articulo/<int:article_id>', views.article, name="article_from_blog_view"),
]
