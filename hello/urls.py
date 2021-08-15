from django.urls import path

from .views import *


app_name = 'poll'
urlpatterns = [
    path('', PollsIndex.as_view(), name='index'),
    path('<int:pk>/', PollDetail.as_view(), name='detail'),
    path('<int:pk>/result', PollResult.as_view(), name='result'),
    path('<int:question_id>/vote/', vote, name='vote'),
]