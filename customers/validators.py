import re
from django.core.exceptions import ValidationError


FARSI_REGEX = re.compile(r'^[u0600-u06FFs]+$')

def validate_farsi(value):
    if not FARSI_REGEX.match(value):
        raise ValidationError("this field only accepts farsi!")
