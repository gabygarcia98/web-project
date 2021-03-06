# Generated by Django 3.0.4 on 2020-03-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0008_auto_20200325_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotify_user',
            name='access_token',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='spotify_user',
            name='refresh_token',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='spotify_user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
