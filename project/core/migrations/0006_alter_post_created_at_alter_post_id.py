# Generated by Django 4.1.1 on 2023-08-01 17:58

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_followerscount_alter_post_created_at_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 1, 17, 58, 46, 951413)),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('017577a6-c86e-43de-96f9-8d11922d2654'), primary_key=True, serialize=False),
        ),
    ]
