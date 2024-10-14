from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Survey
from .serializers import SurveyWriteSerializer, SurveyReadSerializer

class SurveyCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Survey.objects.all()
    serializer_class = SurveyWriteSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.person)


class SurveyListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SurveyReadSerializer

    def get_queryset(self):
        return Survey.objects.filter(created_by__user=self.request.user)