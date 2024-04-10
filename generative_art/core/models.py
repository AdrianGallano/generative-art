from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Art(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    resolution_width = models.IntegerField(default=500, validators=[MinValueValidator(20), MaxValueValidator(4000)])
    resolution_height = models.IntegerField(default=500, validators=[MinValueValidator(20), MaxValueValidator(4000)])
    no_of_circles = models.IntegerField(default=1000000, validators=[MinValueValidator(1), MaxValueValidator(4000000)])
    max_color_cycle = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(4000000)])
    parameter_1 = models.IntegerField(default=14, validators=[MinValueValidator(2), MaxValueValidator(50)])
    parameter_2 = models.IntegerField(default=14, validators=[MinValueValidator(2), MaxValueValidator(50)])
    parameter_3 = models.IntegerField(default=20, validators=[MinValueValidator(2), MaxValueValidator(50)])
    parameter_4 = models.IntegerField(default=24, validators=[MinValueValidator(2), MaxValueValidator(50)])
    parameter_5 = models.IntegerField(default=54, validators=[MinValueValidator(2), MaxValueValidator(100)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title