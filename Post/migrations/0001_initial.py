

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textContent', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('pictureContent', models.FileField(upload_to='images')),
                ('date_Modified', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_author', to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='channel.Channel')),
                ('voteDown', models.ManyToManyField(blank=True, related_name='voteDown', to=settings.AUTH_USER_MODEL)),
                ('voteUp', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.IntegerField(null=True)),
                ('content', models.TextField()),
                ('picture', models.FileField(upload_to='images')),
                ('time', models.DateField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment_authour', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.Card')),
                ('voteDown', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('voteUp', models.ManyToManyField(blank=True, related_name='voteUp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
