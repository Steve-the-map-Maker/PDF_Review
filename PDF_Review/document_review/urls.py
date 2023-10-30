from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'document_versions', views.DocumentVersionViewSet),

print("URLs in document_review are being processed.")
urlpatterns = [
    path('', include(router.urls)),
    path('frontend/', TemplateView.as_view(template_name="index.html")),
    path('frontend/', views.FrontendView.as_view(), name='frontend'),
]
