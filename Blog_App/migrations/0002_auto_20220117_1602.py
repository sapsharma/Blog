# Generated by Django 3.2.6 on 2022-01-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_a',
            name='Blog_Desc1',
            field=models.TextField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='blog_a',
            name='Blog_Desc',
            field=models.TextField(max_length=500),
        ),
    ]
