# Generated by Django 2.2.3 on 2019-07-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190717_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='testParam',
            field=models.IntegerField(default=1209),
            preserve_default=False,
        ),
    ]
