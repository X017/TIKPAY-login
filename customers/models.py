from django.core.exceptions import ValidationError
from django.db import models



class Customer(models.Model):
    faFirstName = models.CharField(max_length = 150)
    faLastName = models.CharField(max_length = 150)
    enFirstName = models.CharField(max_length = 200)
    enLastName  = models.CharField(max_length = 200)
    email       = models.EmailField(max_length = 300)
    faFatherName= models.CharField(max_length = 100)
    birthDay    = models.DateField()
    nationalCode = models.CharField(max_length=10) 
    mobile       = models.CharField(max_length=10)
    phone        = models.CharField(max_length=10)
    address      = models.TextField(null=False)
    cardNumber   = models.CharField(max_length=16)
    shabaNumber  = models.CharField(max_length=24)
    faTerminalName = models.CharField(max_length=100)
    enTerminalName = models.CharField(max_length=120)  
    file = models.FileField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.enLastName} - {self.enFirstName}"    
        
    class Meta:
        ordering = ['-created_at']



