from django.db import models


# Create your models here.
class Academic(models.Model):
    academic_id = models.AutoField
    academic_name = models.TextField()
    desc = models.TextField()
    fileupload = models.FileField(upload_to="portal/static/Documents", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.academic_name


class Syllabus(models.Model):
    syllabus_id = models.AutoField
    syllabus_name = models.TextField()
    desc = models.TextField()
    fileupload = models.FileField(upload_to="portal/static/Documents", default="")
    pub_date = models.DateField()
