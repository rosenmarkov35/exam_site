from django.contrib import admin

from exam_site.review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
