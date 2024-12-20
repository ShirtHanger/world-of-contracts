# Generated by Django 5.1.4 on 2024-12-10 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_agent_age_alter_agent_agent_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('type', models.CharField(choices=[('V', 'Versatile Gadget'), ('T', 'Tracking'), ('W', 'Melee Weapon'), ('F', 'Firearm'), ('H', 'Hacking'), ('S', 'Surveillance'), ('E', 'Explosive'), ('L', 'Listening Bug'), ('D', 'Disguise Kit'), ('M', 'Medical Kit'), ('C', 'Communication'), ('S', 'Surveillance'), ('D', 'Stealth'), ('L', 'Lockpicking')], default='V', max_length=1)),
                ('manufacturer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='agent',
            name='age',
            field=models.IntegerField(default=36),
        ),
        migrations.AlterField(
            model_name='agent',
            name='description',
            field=models.TextField(default='[DATA EXPUNGED]', max_length=1000),
        ),
        migrations.AlterField(
            model_name='agent',
            name='gender',
            field=models.CharField(default='[Clearence Required]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='height_cm',
            field=models.IntegerField(default=184),
        ),
        migrations.AlterField(
            model_name='agent',
            name='place_of_birth',
            field=models.CharField(default='[Classified]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='previous_agency',
            field=models.CharField(default='[Clearence Required]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='real_name',
            field=models.CharField(default='[DATA EXPUNGED]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='region',
            field=models.CharField(default='[DATA EXPUNGED]', max_length=100),
        ),
        migrations.AlterField(
            model_name='agent',
            name='weight_kg',
            field=models.IntegerField(default=99),
        ),
    ]
