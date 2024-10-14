from django.urls import path
from .views import (
    DescriptiveQuestionCreateView,
    MultipleChoiceQuestionCreateView,
    NumericQuestionCreateView,
    MatrixQuestionCreateView,
)

urlpatterns = [
    path('descriptive/', DescriptiveQuestionCreateView.as_view(), name='descriptive-question-create'),
    path('multiple-choice/', MultipleChoiceQuestionCreateView.as_view(), name='multiple-choice-question-create'),
    path('numeric/', NumericQuestionCreateView.as_view(), name='numeric-question-create'),
    path('matrix/', MatrixQuestionCreateView.as_view(), name='matrix-question-create'),
]
