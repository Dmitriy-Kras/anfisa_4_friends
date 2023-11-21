# Generated by Django 3.2.16 on 2023-11-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_auto_20231121_0936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'объект обёртка', 'verbose_name_plural': 'Обёртки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, help_text='Чем меньше цифра тем выше отображение на сайте ', verbose_name='Порядок отображения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='слаг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='Обязательное поле', max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='title',
            field=models.CharField(help_text='Обязательное поле', max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.Topping', verbose_name='топпинги'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='slug',
            field=models.SlugField(max_length=64, unique=True, verbose_name='слаг'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='title',
            field=models.CharField(help_text='Обязательное поле', max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='название'),
        ),
    ]