# Generated by Django 4.1.1 on 2022-09-28 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_userratingmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='userratingmovie',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.movie'),
        ),
    ]
