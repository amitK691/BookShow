# Generated by Django 3.2.1 on 2021-05-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_trendposter_playlogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newarrivalbelow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=255, null=True)),
                ('Duration', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Poster', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
