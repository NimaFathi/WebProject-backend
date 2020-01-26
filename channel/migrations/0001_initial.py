# Generated by Django 3.0.2 on 2020-01-26 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Post', '0007_remove_comment_children'),
        ('UserProfile', '0002_userprofile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('rules', models.CharField(max_length=50)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='UserProfile.UserProfile')),
                ('authours', models.ManyToManyField(related_name='authors', to='UserProfile.UserProfile')),
                ('posts', models.ManyToManyField(to='Post.Card')),
            ],
        ),
    ]
