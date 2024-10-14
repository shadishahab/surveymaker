from django.db import models

from questions.models import (
    Choice,
    MatrixColumn,
    MatrixRow,
    DescriptiveQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
    )
from surveys.models import Survey

class Response(models.Model):
    submitted_at = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(
        Survey,
        related_name='responses',
        on_delete=models.CASCADE
        )
    
    class Meta:
        ordering = ['survey']

    def __str__(self):
        return f"Response to {self.survey.title} at {self.submitted_at}"
    

class Answer(models.Model):
    response = models.ForeignKey(
        Response,
        related_name='%(class)ss',
        on_delete=models.CASCADE
        )

    class Meta:
        abstract = True


class DescriptiveAnswer(Answer):
    answer_text = models.TextField()
    question = models.ForeignKey(
        DescriptiveQuestion,
        related_name='answers',
        on_delete=models.CASCADE
        )
    
    class Meta:
        verbose_name = 'Descriptive Answer'
        verbose_name_plural = 'Descriptive Answers'
        ordering = ['id']

    def __str__(self):
        return self.answer_text


class MultipleChoiceAnswer(Answer):
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(
        MultipleChoiceQuestion,
        related_name='answers',
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'Multiple Choice Answer'
        verbose_name_plural = 'Multiple Choice Answers'
        ordering = ['id']

    def __str__(self):
        return self.selected_choice


class NumericAnswer(Answer):
    numeric_value = models.IntegerField()
    question = models.ForeignKey(
        NumericQuestion,
        related_name='answers',
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'Numeric Answer'
        verbose_name_plural = 'Numeric Answers'
        ordering = ['id']

    def __str__(self):
        return self.numeric_value

#It doesn't inherit from Answer. Because it is already indirectly related to MatrixQuestion through 'row' and 'column'. So we don't need a direct FK to Question in this model.
class MatrixAnswer(models.Model):
    response = models.ForeignKey(
        Response,
        related_name='matrixanswers',
        on_delete=models.CASCADE
        )
    row = models.ForeignKey(
        MatrixRow,
        related_name='answers',
        on_delete=models.CASCADE
        )
    column = models.ForeignKey(
        MatrixColumn,
        related_name='answers',
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'Matrix Answer'
        verbose_name_plural = 'Matrix Answers'
        ordering = ['id']

    def __str__(self):
        return f"Answer to {self.row.row_text} - {self.column.column_text}"
