# Generated by Django 3.1.7 on 2021-04-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210430_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.CharField(default=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(default=True, max_length=70),
        ),
    ]
