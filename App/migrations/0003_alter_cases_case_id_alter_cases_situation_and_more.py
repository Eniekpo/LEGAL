# Generated by Django 4.1.3 on 2023-02-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_client_gender_alter_lawyer_gender_cases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='case_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cases',
            name='situation',
            field=models.CharField(choices=[('', 'Case Status'), ('Completed', 'Completed'), ('InProgress', 'InProgress'), ('Dismissed', 'Dismissed')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='Password',
            field=models.CharField(max_length=16),
        ),
    ]
