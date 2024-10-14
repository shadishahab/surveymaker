from django.db import models

from surveys.models import Survey

class Question(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField()
    is_required = models.BooleanField(default=True)
    survey = models.ForeignKey(
        Survey,
        related_name='%(class)ss',
        on_delete=models.CASCADE
        )

    class Meta:
        abstract = True
        ordering = ['order']


class DescriptiveQuestion(Question):
    # (No additional fields are needed)
    class Meta:
        verbose_name = 'Descriptive Question'
        verbose_name_plural = 'Descriptive Questions'

    def __str__(self):
        return self.title


class MultipleChoiceQuestion(Question):
    # (Choices will be linked via a separate model)
    class Meta:
        verbose_name = 'Multiple Choice Question'
        verbose_name_plural = 'Multiple Choice Questions'

    def __str__(self):
        return self.title


class NumericQuestion(Question):
    min_value = models.IntegerField()
    max_value = models.IntegerField()

    class Meta:
        verbose_name = 'Numeric Question'
        verbose_name_plural = 'Numeric Questions'


class MatrixQuestion(Question):

    class Meta:
        verbose_name = 'Matrix Question'
        verbose_name_plural = 'Matrix Questions'

    def __str__(self):
        return self.title


class MatrixRow(models.Model):
    row_text = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField()
    matrix_question = models.ForeignKey(
        MatrixQuestion,
        related_name='rows',
        on_delete=models.CASCADE
        )
    
    class Meta:
        verbose_name = 'Matrix Row'
        verbose_name_plural = 'Matrix Rows'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.matrix_question.title} - {self.row_text}"


class MatrixColumn(models.Model):
    column_text = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField()
    matrix_question = models.ForeignKey(
        MatrixQuestion,
        related_name='columns',
        on_delete=models.CASCADE
        )
    
    class Meta:
        verbose_name = 'Matrix Column'
        verbose_name_plural = 'Matrix Columns'
        ordering = ['order']

    def __str__(self):
        return f"{self.matrix_question.title} - {self.column_text}"


class Choice(models.Model):
    text = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField()
    question = models.ForeignKey(
        MultipleChoiceQuestion,
        related_name='choices',
        on_delete=models.CASCADE
        )
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text

