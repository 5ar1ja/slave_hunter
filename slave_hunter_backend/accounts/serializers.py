from rest_framework import serializers
from .models import Company

#сериализатор для модели Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('owner','created_at', 'updated_at')

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Company name cannot be empty.")
        return value