from rest_framework import serializers
from .models import Url


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = (
            'id', 
            'long',
            'short',
            'created_at',
            'expire_at',
            'ip',
            'domain',
            'redirect_number'
        )