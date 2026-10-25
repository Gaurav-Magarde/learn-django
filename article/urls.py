from django.urls import path
from .views import ArticleListAPIView,ArticleCreateAPIView,ArticleUpdateAPIView,ArticleDeleteAPIView


urlpatterns = [
    path('',ArticleListAPIView.as_view(),name='article-list'),
    path('create/',ArticleCreateAPIView.as_view(),name='article-create'),
    path('<str:pk>/update/',ArticleUpdateAPIView.as_view(),name='article-update'),
    path('<str:pk>/delete/',ArticleDeleteAPIView.as_view(),name='article-delete'),
]