from rest_framework import serializers
from .models import Book


# Automatically create a Serializer class with all the fields in the Book model
# HyperlinkedModelSerializer uses hyperlinks to represent relationships rather than primary keys
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")

        return value
