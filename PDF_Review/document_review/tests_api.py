from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import CustomUser, Document, Comment, DocumentVersion  # Corrected import


class DocumentReviewAPITest(APITestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(
            username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a document
        self.document = Document.objects.create(
            title='Test Document',
            file='path/to/file',
            upload_date='2022-01-01T00:00:00Z',
            owner=self.user
        )

        # Create a comment
        self.comment = Comment.objects.create(
            content='Test Comment',
            page_number=1,
            coordinates='0,0',
            created_at='2022-01-01T00:00:00Z',
            document=self.document,
            author=self.user
        )

    # Test to create a new document
    def test_create_document(self):
        # Create an in-memory uploaded file
        file = SimpleUploadedFile(
            "file.pdf", b"file_content", content_type="application/pdf")

        data = {'title': 'New Test Document',
                'file': file, 'owner': self.user.id}
        url = reverse('document-list')
        response = self.client.post(
            url, data, format='multipart')  # Note the format
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test to read a document
    def test_read_document(self):
        url = reverse('document-detail', args=[self.document.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test to update a document
    def test_update_document(self):
        # Create an in-memory uploaded file for the update
        file = SimpleUploadedFile(
            "updated_file.pdf", b"updated_file_content", content_type="application/pdf")

        url = reverse('document-detail', args=[self.document.id])
        data = {'title': 'Updated Test Document',
                'file': file, 'owner': self.user.id}
        response = self.client.put(
            url, data, format='multipart')  # Note the format
        print(response.data)  # For debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test to delete a document
    def test_delete_document(self):
        url = reverse('document-detail', args=[self.document.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
