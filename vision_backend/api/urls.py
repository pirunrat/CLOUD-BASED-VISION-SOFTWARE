from django.urls import path
from .views import run_model, video_stream,receive_frame
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('video_stream/', video_stream),
    path('receive_frame/', receive_frame)
    # path('model/', run_model),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
