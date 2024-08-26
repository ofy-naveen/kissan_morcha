from django.contrib import admin
from .models import ImageUpload

@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('image', 'uploaded_at')
    search_fields = ('uploaded_at',)
    list_filter = ('uploaded_at',)
