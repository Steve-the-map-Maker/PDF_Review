from django.contrib.auth.models import AbstractUser
from django.db import models

# User model


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="customuser_set",
        related_query_name="user",
    )


user_permissions = models.ManyToManyField(
    'auth.Permission',
    blank=True,
    help_text='Specific permissions for this user.',
    related_name="customuser_set",
    related_query_name="user",
)


# Document model


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        CustomUser, related_name='documents', on_delete=models.CASCADE)

# Comment model


class Comment(models.Model):
    content = models.TextField()
    page_number = models.IntegerField()
    coordinates = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document = models.ForeignKey(
        Document, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        CustomUser, related_name='comments', on_delete=models.CASCADE)

# DocumentVersion model


class DocumentVersion(models.Model):
    document = models.ForeignKey(
        Document, related_name='versions', on_delete=models.CASCADE)
    version_number = models.IntegerField()
    file = models.FileField(upload_to='document_versions/')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser, related_name='created_versions', on_delete=models.CASCADE)
