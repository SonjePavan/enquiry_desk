# Generated by Django 3.1.3 on 2020-12-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='extra',
            field=models.TextField(default='extra', max_length=50),
            preserve_default=False,
        ),
    ]
