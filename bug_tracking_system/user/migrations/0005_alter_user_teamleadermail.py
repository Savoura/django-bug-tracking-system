# Generated by Django 4.0.5 on 2022-09-13 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_remove_team_teamleader_team_teamleadermail'),
        ('user', '0004_alter_user_teamleadermail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='teamleadermail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='team.team'),
        ),
    ]
