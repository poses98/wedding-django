# Generated by Django 3.1.5 on 2021-03-18 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_auto_20210318_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmacion',
            name='have_a_partner',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='partner_name',
        ),
        migrations.RemoveField(
            model_name='confirmacion',
            name='partner_surname',
        ),
    ]
