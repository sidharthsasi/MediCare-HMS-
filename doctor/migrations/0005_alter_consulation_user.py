# Generated by Django 4.1.2 on 2022-11-02 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_patient_blood_group'),
        ('doctor', '0004_alter_consulation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.appointment'),
        ),
    ]