from django.db import models
from hasher.sizeChecker import ContentTypeRestrictedFileField


# Create your models here.
# class Hash(models.Model):
#     sha = models.CharField(max_length=255, blank=True)

class Document(models.Model):
    # number_of_loads = models.IntegerField()
    document = ContentTypeRestrictedFileField(max_upload_size=10240, upload_to='documents/', )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    sha = models.CharField(max_length=255, blank=True)

