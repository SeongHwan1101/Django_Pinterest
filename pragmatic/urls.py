from django.views.generic import TemplateView
from pip.__main__ import path

from accountapp.views import ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView




urlpatterns = {
    path('list/', ArticleListView.as_view(), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),
    path('list/', ArticleDetailView.as_view(), name='detail'),
    path('list/', ArticleUpdateView.as_view(), name='update'),
    path('list/', ArticleDeleteView.as_view(), name='delete'),

}