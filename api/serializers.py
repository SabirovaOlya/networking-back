from rest_framework import serializers
from .models import ApiModel


class ApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = '__all__'

