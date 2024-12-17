from rest_framework import serializers
from customers.models import Customer
import re

FARSI_REGEX = re.compile(r'^[u0600-u06FFs]+$')
def validate_farsi(value):
    if FARSI_REGEX.match(value):
        raise serializers.ValidationError("some inputs must be farsi")



class CustomerSerializer(serializers.ModelSerializer):
    faFirstName = serializers.CharField(validators=[validate_farsi])
    class Meta:
        model = Customer
        fields = [
            'faFirstName',
            'faLastName',
            'enFirstName',
            'enLastName',
            'email',
            'faFatherName',
            'birthDay',
            'nationalCode',
            'mobile',
            'phone',
            'address',
            'cardNumber',
            'shabaNumber',
            'faTerminalName',
            'enTerminalName',
            'id',
        ]
        read_only_fields = ['id']
    def validate_phone(self,value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must have exactly 10 numbers and no alphabets")
        return value


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['file']

