# Generated by Django 3.1.2 on 2020-10-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
