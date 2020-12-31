from django.db import models

# Create your models here.
class Academic(models.Model):
    academic_id = models.AutoField
    academic_name = models.CharField(max_length=200)
    desc = models.TextField ()
    fileupload = models.FileField(upload_to="portal/static/Documents",default="")
    pub_date = models.DateField()

