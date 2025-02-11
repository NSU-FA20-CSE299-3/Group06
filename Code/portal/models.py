from django.db import models


# Create your models here.
class Class_routine(models.Model):
    class_routine_id = models.AutoField
    class_routine_name = models.TextField()
    desc = models.TextField()
    fileupload = models.FileField(upload_to="portal/static/Documents", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.class_routine_name


class Syllabus(models.Model):
    syllabus_id = models.AutoField
    syllabus_name = models.TextField()
    desc = models.TextField()
    fileupload = models.FileField(upload_to="portal/static/Documents", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.syllabus_name


class Employment(models.Model):
    employment_id = models.AutoField
    employment_name = models.TextField()
    desc = models.TextField()
    fileupload = models.FileField(upload_to="portal/static/Documents", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.employment_name


class About(models.Model):
    about_id = models.AutoField
    about_name = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.about_name
