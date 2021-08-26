# Generated by Django 3.2.6 on 2021-08-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MapAnnotationPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('latitude', models.IntegerField()),
                ('number', models.CharField(max_length=10)),
                ('streetAddress', models.CharField(max_length=50)),
                ('wishList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.wishlist')),
            ],
        ),
    ]
