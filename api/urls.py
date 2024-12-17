from django.urls import path
from api.v1 import views

urlpatterns = [
        path('v1/sign-up/',views.SignUpAPI.as_view()),
        path('v1/upload/<int:pk>/',views.UploadSingUPAPI.as_view()),
]


