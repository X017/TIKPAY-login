from rest_framework import serializers
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from customers.models import Customer
from .serializers import CustomerSerializer, PictureSerializer

class SignUpAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            return Response({"user.id":user.id}, status=status.HTTP_201_CREATED)

 # return Response({"REQUEST":400}, status=status.HTTP_400_BAD_REQUEST)

class UploadSingUPAPI(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = PictureSerializer
    lookup_field = 'pk'
    def get_object(self, *arg, **kwargs):
         return generics.get_object_or_404(Customer, pk=self.kwargs.get('pk'))
