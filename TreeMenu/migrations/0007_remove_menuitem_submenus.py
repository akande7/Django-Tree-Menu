# Generated by Django 4.0.4 on 2023-03-04 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TreeMenu', '0006_remove_menu_submenus_menuitem_submenus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='submenus',
        ),
    ]