from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=255)  
    title = models.CharField(max_length=255, blank=True, null=True)  
    message = models.TextField() 
    image = models.ImageField(upload_to='img/', blank=True, null=True) 
    date_created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name
