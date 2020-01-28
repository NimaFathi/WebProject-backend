from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('avatar', models.ImageField(default='path/to/my/default/image.jpg', upload_to='')),
                ('user_email', models.EmailField(max_length=254)),
                ('occupy', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=50)),
            ],
        ),
    ]
