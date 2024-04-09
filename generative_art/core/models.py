from django.db import models
from django.contrib.auth.models import User

class Art(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    resolution_width = models.IntegerField(default=500)
    resolution_height = models.IntegerField(default=500)
    no_of_circles = models.IntegerField(default=100000)
    max_color_cycle = models.IntegerField(default=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title