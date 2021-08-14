# Generated by Django 3.2.6 on 2021-08-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0002_auto_20210813_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='color',
            field=models.CharField(choices=[('beige', 'Beige'), ('red', 'Red'), ('purple', 'Purple')], max_length=20, null='True', verbose_name='색상'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='size',
            field=models.CharField(choices=[('L', 'Large'), ('S', 'Small'), ('M', 'Medium')], max_length=10, null='True', verbose_name='사이즈'),
        ),
        migrations.AlterField(
            model_name='review',
            name='satisfaction',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('1', '1'), ('2', '2')], max_length=10, verbose_name='만족도'),
        ),
    ]