from django.urls import path
from .views import ApiView, ApiDetail


urlpatterns = [
    path('', ApiView.as_view(), name='api'),
    path('<int:pk>', ApiDetail.as_view(), name='api-model-detail'),
]
