# Generated by Django 5.1.4 on 2024-12-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_alter_agent_age_alter_agent_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='age',
            field=models.IntegerField(default=27),
        ),
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.TextField(default='[Classified]', max_length=5000),
        ),
        migrations.AlterField(
            model_name='agent',
            name='gender',
            field=models.CharField(default='[DATA EXPUNGED]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='height_cm',
            field=models.IntegerField(default=173),
        ),
        migrations.AlterField(
            model_name='agent',
            name='place_of_birth',
            field=models.CharField(default='[Clearence Required]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='previous_agency',
            field=models.CharField(default='[Undisclosed]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='real_name',
            field=models.CharField(default='[DATA EXPUNGED]', max_length=100),
        ),
        migrations.AlterField(
            model_name='mission',
            name='debrief',
            field=models.TextField(default='[Clearence Required]', max_length=7000),
        ),
        migrations.AlterField(
            model_name='mission',
            name='location',
            field=models.CharField(default='[DATA EXPUNGED]', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='objective',
            field=models.CharField(default='[DATA EXPUNGED]', max_length=255),
        ),
    ]
