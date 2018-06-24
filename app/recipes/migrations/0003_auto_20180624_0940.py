# Generated by Django 2.0.5 on 2018-06-24 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20180624_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Cheese 이름을 저장합니다.', max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'bread',
            },
        ),
        migrations.CreateModel(
            name='Sauces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Sauce의 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='100자까지 Topping의 이름을 저장합니다.', max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='toasting',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bread',
            name='name',
            field=models.CharField(help_text='100자까지 Bread 이름을 저장합니다.', max_length=100),
        ),
        migrations.AlterField(
            model_name='vegetables',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='vegetables',
            name='name',
            field=models.CharField(help_text='100자까지 Vegetable의 이름을 저장합니다.', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cheese',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.Cheese', verbose_name='치즈'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='sauces',
            field=models.ManyToManyField(blank=True, to='recipes.Sauces', verbose_name='소스'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='recipes.Toppings', verbose_name='토핑'),
        ),
    ]
