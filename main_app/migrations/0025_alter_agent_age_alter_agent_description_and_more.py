# Generated by Django 5.1.4 on 2024-12-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_agent_age_alter_agent_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='age',
            field=models.IntegerField(default=47),
        ),
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.TextField(default='[RESTRICTED]', max_length=5000),
        ),
        migrations.AlterField(
            model_name='agent',
            name='gender',
            field=models.CharField(default='[FORBIDDEN]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='place_of_birth',
            field=models.CharField(default='[FORBIDDEN]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='previous_agency',
            field=models.CharField(default='[FORBIDDEN]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='race_or_ethnicity',
            field=models.CharField(choices=[('R', '[SENSITIVE INFORMATION]'), ('W', 'White/Caucasian'), ('B', 'Black/African Descent'), ('E', 'East Asian'), ('S', 'South Asian/Desi'), ('M', 'Middle Eastern/Semitic'), ('L', 'Latino/Hispanic'), ('I', 'Indigenous/Native '), ('O', 'Other/Mixed')], default='R', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='real_name',
            field=models.CharField(default='[FORBIDDEN]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='region',
            field=models.CharField(default='[FORBIDDEN]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='weight_kg',
            field=models.IntegerField(default=78),
        ),
        migrations.AlterField(
            model_name='mission',
            name='debrief',
            field=models.TextField(default='[RESTRICTED]', max_length=7000),
        ),
        migrations.AlterField(
            model_name='mission',
            name='location',
            field=models.CharField(default='[CLEARANCE REQUIRED]', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='objective',
            field=models.CharField(default='[NOT AVAILABLE]', max_length=255),
        ),
        migrations.AlterField(
            model_name='mission',
            name='urgency',
            field=models.CharField(choices=[('R', '[SENSITIVE INFORMATION]'), ('T', 'Trivial'), ('L', 'Low Priority'), ('M', 'Medium Priority'), ('H', 'High Priority'), ('C', 'Critical'), ('E', 'Emergency')], default='R', max_length=1),
        ),
    ]
