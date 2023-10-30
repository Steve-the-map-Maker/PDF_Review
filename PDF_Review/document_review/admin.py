from django.contrib import admin
from .models import CustomUser, Document, Comment, DocumentVersion


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Document)
admin.site.register(Comment)
admin.site.register(DocumentVersion)
