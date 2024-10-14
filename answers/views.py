from rest_framework.generics import CreateAPIView
from .models import DescriptiveAnswer, MatrixAnswer, MultipleChoiceAnswer, NumericAnswer, Response
from .serializers import DescriptiveAnswerSerializer, MatrixAnswerSerializer, MultipleChoiceAnswerSerializer, NumericAnswerSerializer, ResponseSerializer

class ResponseCreateAPIView(CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class ResponseListAPIView(CreateAPIView):
    serializer_class = ResponseSerializer

    def get_queryset(self):
        survey_id = self.kwargs['survey_id']
        return Response.objects.filter(survey_id=survey_id)


class DescriptiveAnswerCreateAPIView(CreateAPIView):
    queryset = DescriptiveAnswer.objects.all()
    serializer_class = DescriptiveAnswerSerializer


class MultipleChoiceAnswerCreateAPIView(CreateAPIView):
    queryset = MultipleChoiceAnswer.objects.all()
    serializer_class = MultipleChoiceAnswerSerializer


class NumericAnswerCreateAPIView(CreateAPIView):
    queryset = NumericAnswer.objects.all()
    serializer_class = NumericAnswerSerializer


class MatrixAnswerCreateAPIView(CreateAPIView):
    queryset = MatrixAnswer.objects.all()
    serializer_class = MatrixAnswerSerializer