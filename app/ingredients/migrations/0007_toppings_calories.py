# Generated by Django 2.1.2 on 2018-10-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_auto_20180926_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppings',
            name='calories',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
