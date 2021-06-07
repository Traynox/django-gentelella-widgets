# Generated by Django 3.1.11 on 2021-06-04 17:32

from django.db import migrations


def update_icons(apps, schema_editor):
    model = apps.get_model('djgentelella', 'MenuItem')
    logout = model.objects.filter(title='Logout').first()
    if logout is not None:
        logout.only_icon=False
        logout.save()

    help = model.objects.filter(icon='fa fa-envelope-o').first()
    if help is not None:
        help.title = 'Help'
        help.save()

class Migration(migrations.Migration):

    dependencies = [
        ('djgentelella', '0006_permissionscategorymanagement'),
    ]

    operations = [
        migrations.RunPython(update_icons),
    ]