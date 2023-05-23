# Generated by Django 4.2.1 on 2023-05-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_projectlist_code_projectlist_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyectlist',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('code', models.TextField(default='')),
                ('date', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='projectlist',
        ),
    ]