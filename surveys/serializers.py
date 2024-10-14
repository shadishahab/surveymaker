from rest_framework import serializers
from .models import Survey

class SurveyWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['title', 'description', 'created_at']
        read_only_fields = ['created_by']


class SurveyReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'