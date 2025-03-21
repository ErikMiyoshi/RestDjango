# Generated by Django 5.1.7 on 2025-03-21 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_reciperequirement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem')),
            ],
        ),
    ]
