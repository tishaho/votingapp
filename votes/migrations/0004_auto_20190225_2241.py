# Generated by Django 2.1.7 on 2019-02-25 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_auto_20190218_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='partylist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partylist', to='votes.Partylist'),
        ),
    ]