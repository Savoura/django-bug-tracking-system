# Generated by Django 4.0.5 on 2022-09-13 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_teamleadermail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='teamleadermail',
            new_name='team',
        ),
    ]