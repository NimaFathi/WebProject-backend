from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('textContent', models.TextField()),
                ('creatorPicture', models.FileField(upload_to='images')),
                ('adminId', models.IntegerField()),
                ('authorId', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('creatorName', models.CharField(max_length=50)),
                ('pictureContent', models.FileField(upload_to='images')),
                ('date_Modified', models.DateTimeField(auto_now_add=True)),
                ('voteDown', models.ManyToManyField(blank=True, related_name='voteDown', to=settings.AUTH_USER_MODEL)),
                ('voteUp', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('parentId', models.IntegerField(null=True)),
                ('userId', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('picture', models.FileField(upload_to='images')),
                ('time', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Card')),
                ('voteDown', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('voteUp', models.ManyToManyField(blank=True, related_name='voteUp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
