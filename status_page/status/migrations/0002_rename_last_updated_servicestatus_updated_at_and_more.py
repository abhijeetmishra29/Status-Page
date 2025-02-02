# Generated by Django 5.1.2 on 2025-02-01 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicestatus',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='servicestatus',
            name='name',
        ),
        migrations.AddField(
            model_name='servicestatus',
            name='service',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='status.service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('operational', 'Operational'), ('maintenance', 'Under Maintenance'), ('down', 'Down')], default='operational', max_length=20),
        ),
        migrations.AlterField(
            model_name='servicestatus',
            name='status',
            field=models.CharField(choices=[('operational', 'Operational'), ('maintenance', 'Under Maintenance'), ('down', 'Down')], default='operational', max_length=20),
        ),
    ]
