# Generated by Django 5.1.4 on 2024-12-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_agent_age_alter_agent_agent_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='age',
            field=models.IntegerField(default=37),
        ),
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.TextField(default='[DATA EXPUNGED], [Classified]', max_length=1000),
        ),
        migrations.AlterField(
            model_name='agent',
            name='height_cm',
            field=models.IntegerField(default=173),
        ),
        migrations.AlterField(
            model_name='agent',
            name='region',
            field=models.CharField(default='[REDACTED]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='weight_kg',
            field=models.IntegerField(default=78),
        ),
    ]
