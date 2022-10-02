# Generated by Django 4.1.1 on 2022-10-01 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0009_userratingserial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReviewMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_type', models.CharField(choices=[('Positive', 'Positive'), ('Neutral', 'Neutral'), ('Negative', 'Negative')], max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=2500)),
                ('movie', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.movie')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
