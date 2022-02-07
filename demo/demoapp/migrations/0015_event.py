# Generated by Django 3.2.11 on 2022-01-17 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0014_chunkeduploaditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
