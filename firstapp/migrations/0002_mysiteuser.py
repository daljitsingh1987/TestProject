# Generated by Django 2.0.6 on 2019-09-19 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySiteUser',
            fields=[
                ('userFullName', models.CharField(default='', max_length=200)),
                ('userEmail', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('userPassword', models.CharField(default='', max_length=200)),
                ('userMobile', models.BigIntegerField()),
                ('isActive', models.BooleanField(default=True)),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.UserRole')),
            ],
        ),
    ]
