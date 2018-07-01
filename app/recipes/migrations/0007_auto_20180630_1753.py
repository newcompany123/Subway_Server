# Generated by Django 2.0.5 on 2018-06-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20180630_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sandwich',
            old_name='image',
            new_name='image3x_left',
        ),
        migrations.RenameField(
            model_name='sandwich',
            old_name='image3x',
            new_name='image3x_right',
        ),
        migrations.AddField(
            model_name='bread',
            name='image3x',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cheese',
            name='image3x',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainingredient',
            name='image',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainingredient',
            name='image3x',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='image_left',
            field=models.FilePathField(default='', max_length=255, path='sandwich'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sandwich',
            name='image_right',
            field=models.FilePathField(default='', max_length=255, path='sandwich'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sauces',
            name='image3x',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toppings',
            name='image3x',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vegetables',
            name='image3x',
            field=models.FilePathField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainingredient',
            name='name',
            field=models.CharField(help_text='100까지 MainIngredient의 이름을 저장합니다.', max_length=100),
        ),
        migrations.AlterField(
            model_name='mainingredient',
            name='quantity',
            field=models.CharField(blank=True, help_text='100자까지 MainIngredient의 quantity를 저장합니다.', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='mainingredient',
            unique_together={('name', 'quantity')},
        ),
    ]
