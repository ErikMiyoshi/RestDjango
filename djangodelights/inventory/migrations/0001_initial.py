# Generated by Django 5.1.7 on 2025-03-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(max_length=5)),
                ('price', models.FloatField()),
            ],
        ),
    ]
