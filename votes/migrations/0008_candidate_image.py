# Generated by Django 2.1.7 on 2019-03-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20190304_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]