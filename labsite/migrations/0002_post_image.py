# Generated by Django 2.0.5 on 2018-05-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]
