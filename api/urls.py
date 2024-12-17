from django.urls import path
from api.v1 import views

urlpatterns = [
        path('sign-up/',views.SignUpAPI.as_view()),
        path('upload/<int:pk>/',views.UploadSingUPAPI.as_view()),
]


