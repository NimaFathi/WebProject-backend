# Generated by Django 2.2 on 2020-01-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='images/AI_HW1.png', upload_to='images'),
        ),
    ]
