from rest_framework import serializers
from .models import (
    Response,
    DescriptiveAnswer,
    NumericAnswer,
    MatrixAnswer,
    MultipleChoiceAnswer)

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class DescriptiveAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptiveAnswer
        fields = ['id', 'response', 'question', 'answer_text']


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceAnswer
        fields = ['id', 'response', 'question', 'selected_choice']


class NumericAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericAnswer
        fields = ['id', 'response', 'question', 'numeric_value']


class MatrixAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatrixAnswer
        fields = ['id', 'response', 'row', 'column']