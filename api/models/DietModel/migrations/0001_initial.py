# Generated by Django 3.2.4 on 2021-09-22 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diet_material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_material_id', models.IntegerField(unique=True, verbose_name='食材id')),
                ('material_id', models.IntegerField(unique=True, verbose_name='物品id')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='食材名')),
            ],
        ),
        migrations.CreateModel(
            name='diet_materialDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(choices=[(1, 'Q1'), (2, 'Q2'), (3, 'Q3')], default=1, verbose_name='食材等级')),
                ('health', models.FloatField(default=0.0, verbose_name='健康度')),
                ('Satiety', models.FloatField(default=0.0, verbose_name='饱食度')),
                ('acid', models.FloatField(default=0.0, verbose_name='酸')),
                ('salty', models.FloatField(default=0.0, verbose_name='咸')),
                ('sweet', models.FloatField(default=0.0, verbose_name='甜')),
                ('bitterness', models.FloatField(default=0.0, verbose_name='苦')),
                ('aroma', models.FloatField(default=0.0, verbose_name='味道度')),
                ('r_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DietModel.diet_material', verbose_name='食品')),
            ],
            options={
                'unique_together': {('r_material', 'level')},
            },
        ),
        migrations.CreateModel(
            name='diet_recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50, verbose_name='名字')),
                ('Owner', models.IntegerField(db_index=True, default=' ', verbose_name='拥有者')),
                ('health', models.FloatField(default=0.0, verbose_name='健康度')),
                ('Satiety', models.FloatField(default=0.0, verbose_name='饱食度')),
                ('acid', models.FloatField(default=0.0, verbose_name='酸')),
                ('salty', models.FloatField(default=0.0, verbose_name='咸')),
                ('sweet', models.FloatField(default=0.0, verbose_name='甜')),
                ('bitterness', models.FloatField(default=0.0, verbose_name='苦')),
                ('aroma', models.FloatField(default=0.0, verbose_name='味道度')),
            ],
        ),
        migrations.CreateModel(
            name='Input_Recipe_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='数量')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DietModel.diet_materialdetail', verbose_name='输入物资')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DietModel.diet_recipe', verbose_name='配方id')),
            ],
            options={
                'verbose_name_plural': '所需食材表',
            },
        ),
        migrations.AddField(
            model_name='diet_recipe',
            name='input',
            field=models.ManyToManyField(related_name='input', through='DietModel.Input_Recipe_Material', to='DietModel.diet_materialDetail', verbose_name='输入'),
        ),
    ]