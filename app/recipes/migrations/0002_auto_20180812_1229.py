# Generated by Django 2.0.5 on 2018-08-12 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='bookmarker',
            field=models.ManyToManyField(related_name='bookmarked_recipe', through='recipes.BookmarkedRecipe', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipe',
            name='bread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.Bread', verbose_name='빵'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cheese',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.Cheese', verbose_name='치즈'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='inventor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='made_recipe', to=settings.AUTH_USER_MODEL, verbose_name='레시피 제작자'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='liker',
            field=models.ManyToManyField(related_name='liked_recipe', through='recipes.LikedRecipe', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.RecipeName', verbose_name='이름'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='sandwich',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.Sandwich', verbose_name='기본 샌드위치'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='sauces',
            field=models.ManyToManyField(to='recipes.Sauces', verbose_name='소스'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='toasting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.Toasting', verbose_name='토스팅'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='toppings',
            field=models.ManyToManyField(to='recipes.Toppings', verbose_name='토핑'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegetables',
            field=models.ManyToManyField(to='recipes.Vegetables', verbose_name='야채'),
        ),
        migrations.AlterUniqueTogether(
            name='mainingredient',
            unique_together={('name', 'quantity')},
        ),
        migrations.AddField(
            model_name='likedrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='likedrecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmarkedrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='bookmarkedrecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
