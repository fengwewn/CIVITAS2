# Generated by Django 3.2.5 on 2021-08-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sideline_record',
            name='every_sideline_all',
            field=models.JSONField(blank=True, null=True, verbose_name='每种副业总次数'),
        ),
    ]