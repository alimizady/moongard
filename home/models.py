from django.db import models
class Tiket(models.Model):
    name=models.CharField(max_length=20)
    transport=models.CharField(max_length=20)
    reserve_date=models.DateTimeField()
    def __str__(self):
        return f"{self.name}-{self.transport}"
# Create your models here. 
