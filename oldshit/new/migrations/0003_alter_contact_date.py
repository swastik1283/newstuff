# Generated by Django 5.0.4 on 2024-07-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_contact_date_alter_contact_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(),
        ),
    ]
