# Generated by Django 4.1.7 on 2023-04-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('num_one', models.IntegerField(null=True)),
                ('num_two', models.IntegerField(null=True)),
                ('num_three', models.IntegerField(null=True)),
                ('num_four', models.IntegerField(null=True)),
                ('num_five', models.IntegerField(null=True)),
                ('win', models.BooleanField(default=False)),
            ],
        ),
    ]
