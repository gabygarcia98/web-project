# Generated by Django 3.0.4 on 2020-03-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0006_artist_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='information',
            field=models.CharField(default='No Artist Information', max_length=200, null=True),
        ),
    ]
