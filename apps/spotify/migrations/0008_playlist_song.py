# Generated by Django 3.0.4 on 2020-03-21 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0007_auto_20200321_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spotify.Song'),
        ),
    ]
