from django.urls import path
from .views import SurveyCreateAPIView, SurveyListAPIView

urlpatterns = [
    path('create/', SurveyCreateAPIView.as_view(), name='survey-create'),
    path('list/', SurveyListAPIView.as_view(), name='survey-create'),
]