from django.db import models

# Create your models here.
class Academic(models.Model):
    academic_id = models.AutoField
    academic_name = models.CharField(max_length=50)
    desc = models.CharField (max_length=300)
    pub_date = models.DateField() 