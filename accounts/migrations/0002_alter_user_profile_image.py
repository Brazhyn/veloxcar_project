# Generated by Django 5.0.1 on 2024-02-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='default/user.jpg', null=True, upload_to='accounts/images'),
        ),
    ]
