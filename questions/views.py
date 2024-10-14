from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import (
    DescriptiveQuestion,
    MultipleChoiceQuestion,
    NumericQuestion,
    MatrixQuestion,
)
from .serializers import (
    DescriptiveQuestionSerializer,
    MultipleChoiceQuestionSerializer,
    NumericQuestionSerializer,
    MatrixQuestionSerializer,
)

class DescriptiveQuestionCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DescriptiveQuestion.objects.all()
    serializer_class = DescriptiveQuestionSerializer


class MultipleChoiceQuestionCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer


class NumericQuestionCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NumericQuestion.objects.all()
    serializer_class = NumericQuestionSerializer


class MatrixQuestionCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MatrixQuestion.objects.all()
    serializer_class = MatrixQuestionSerializer
