# Generated by Django 5.1.4 on 2024-12-09 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_agent_age_alter_agent_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='age',
            field=models.IntegerField(default=24),
        ),
        migrations.AlterField(
            model_name='agent',
            name='height_cm',
            field=models.IntegerField(default=155),
        ),
        migrations.AlterField(
            model_name='agent',
            name='previous_agency',
            field=models.CharField(default='[REDACTED]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='weight_kg',
            field=models.IntegerField(default=89),
        ),
    ]
