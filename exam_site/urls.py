from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("exam_site.common.urls")),
    path('product/', include("exam_site.product.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include('exam_site.auth_app.urls')),
    path('review/', include('exam_site.review.urls')),
    path('second_hand/', include('exam_site.second_hand.urls')),
]
