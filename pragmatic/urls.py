from django.views.generic import TemplateView
from pip.__main__ import path

urlpatterns = {
    path('list/', TemplateView.as_view(template_name'articleapp/list.html'), name='list');
}