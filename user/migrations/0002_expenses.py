# Generated by Django 5.1.5 on 2025-02-01 23:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.DecimalField(decimal_places=2, max_digits=100)),
                ('total_spend', models.DecimalField(decimal_places=2, max_digits=100)),
                ('current_month_spend', models.DecimalField(decimal_places=2, max_digits=100)),
                ('current_month_recieved', models.DecimalField(decimal_places=2, max_digits=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
