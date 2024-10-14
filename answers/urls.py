# answers/urls.py
from django.urls import path
from .views import (
    ResponseCreateAPIView,
    DescriptiveAnswerCreateAPIView,
    MultipleChoiceAnswerCreateAPIView,
    NumericAnswerCreateAPIView,
    MatrixAnswerCreateAPIView,
    ResponseListAPIView,
)

urlpatterns = [
    path('responses/create', ResponseCreateAPIView.as_view(), name='response-create'),
    path('responses/list/<int:survey_id>/', ResponseListAPIView.as_view(), name='response-list'),
    path('descriptive/', DescriptiveAnswerCreateAPIView.as_view(), name='descriptive-answer-create'),
    path('multiple-choice/', MultipleChoiceAnswerCreateAPIView.as_view(), name='multiple-choice-answer-create'),
    path('numeric/', NumericAnswerCreateAPIView.as_view(), name='numeric-answer-create'),
    path('matrix/', MatrixAnswerCreateAPIView.as_view(), name='matrix-answer-create'),
]
