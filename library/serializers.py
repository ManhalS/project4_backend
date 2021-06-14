from django.db.models import fields
from rest_framework import serializers
from .models import Book

class Bookserializere(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=[
            "pk",
            "title",
            "num_pages",
            "isbn",
            "publish_date",
            "FileBook"
        ]
        extra_kwargs = {
            "title": {"required":False},
            "isbn": {"required":False},
            "num_pages":{"required":False},
            "publish_date":{"required":False}
        }
            
     