# Generated by Django 3.1.4 on 2020-12-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='academic',
            name='academic_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='academic',
            name='desc',
            field=models.TextField(),
        ),
    ]
