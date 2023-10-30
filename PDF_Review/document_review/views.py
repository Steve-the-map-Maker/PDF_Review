from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CustomUser, Document, Comment, DocumentVersion
from .serializers import CustomUserSerializer, DocumentSerializer, CommentSerializer, DocumentVersionSerializer
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt  # <-- Import this
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


@method_decorator(csrf_exempt, name='dispatch')  # <-- Add this line
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [AllowAny]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DocumentVersionViewSet(viewsets.ModelViewSet):
    queryset = DocumentVersion.objects.all()
    serializer_class = DocumentVersionSerializer


class FrontendView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        print("FrontendView is being executed.")
        return super().get(request, *args, **kwargs)
