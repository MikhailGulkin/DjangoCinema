# Generated by Django 4.1.1 on 2022-10-02 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_userreviewmovie_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreviewmovie',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]