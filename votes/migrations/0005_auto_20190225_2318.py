# Generated by Django 2.1.7 on 2019-02-25 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0004_auto_20190225_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='partylist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partylists', to='votes.Partylist'),
        ),
    ]
