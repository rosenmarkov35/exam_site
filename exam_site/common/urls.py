from django.urls import path

from exam_site.common.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
