# Generated by Django 2.1.2 on 2018-10-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20181018_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='calories',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
