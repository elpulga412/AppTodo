from django.db.models import fields
from rest_framework import serializers
from photoshare.models import *

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'