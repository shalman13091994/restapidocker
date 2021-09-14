from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers
from store.models import Product


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'

