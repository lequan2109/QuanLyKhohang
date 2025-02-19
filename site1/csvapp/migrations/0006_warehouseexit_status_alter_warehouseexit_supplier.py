# Generated by Django 5.1.2 on 2024-11-14 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0005_warehouseentry_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseexit',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Chờ xử lý'), ('PROCESSING', 'Đang xử lý'), ('COMPLETED', 'Đã xuất')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='warehouseexit',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csvapp.supplier'),
        ),
    ]
