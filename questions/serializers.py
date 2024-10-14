from rest_framework import serializers
from .models import (
    DescriptiveQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
    MatrixQuestion,
    MatrixRow,
    MatrixColumn,
    Choice,
)

class DescriptiveQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptiveQuestion
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = MultipleChoiceQuestion
        fields = ['title', 'description', 'order', 'is_required', 'survey', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])
        multiple_choice_question = MultipleChoiceQuestion.objects.create(**validated_data)
        
        for choice_data in choices_data:
            Choice.objects.create(question=multiple_choice_question, **choice_data)


class NumericQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericQuestion
        fields = '__all__'


class MatrixRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatrixRow
        fields = '__all__'


class MatrixColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatrixColumn
        fields = '__all__'

class MatrixQuestionSerializer(serializers.ModelSerializer):
    rows = MatrixRowSerializer(many=True, read_only=True)
    columns = MatrixColumnSerializer(many=True, read_only=True)

    class Meta:
        model = MatrixQuestion
        fields = ['title', 'description', 'order', 'is_required', 'survey', 'rows', 'columns']

    def create(self, validated_data):
        rows_data = validated_data.pop('rows', [])
        columns_data = validated_data.pop('columns', [])
        matrix_question = MatrixQuestion.objects.create(**validated_data)

        for row_data in rows_data:
            MatrixRow.objects.create(matrix_question=matrix_question, **row_data)

        for column_data in columns_data:
            MatrixColumn.objects.create(matrix_question=matrix_question, **column_data)

        return matrix_question
