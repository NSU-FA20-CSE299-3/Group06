# Generated by Django 3.1.4 on 2021-01-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20210116_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_name', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
