# Generated by Django 2.2.7 on 2019-11-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=4, max_digits=10)),
                ('pmfd', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]
