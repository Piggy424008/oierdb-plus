# Generated by Django 4.1.5 on 2023-07-21 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.CharField(max_length=10)),
                ('uid', models.IntegerField(verbose_name='OIer')),
                ('school', models.IntegerField()),
                ('score', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('Province', models.IntegerField()),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('ProvinceName', models.CharField(max_length=10)),
                ('CityName', models.CharField(max_length=10)),
                ('Score', models.DecimalField(decimal_places=3, max_digits=10, max_length=10)),
                ('id', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OIer',
            fields=[
                ('name', models.CharField(default='', max_length=10)),
                ('gender', models.IntegerField(default=0, max_length=2)),
                ('enroll_middle', models.IntegerField(default=2023, max_length=10)),
                ('CCF_Score', models.DecimalField(decimal_places=3, max_digits=10, max_length=10)),
                ('CCF_level', models.IntegerField(verbose_name=5)),
                ('OIerDB_score', models.DecimalField(decimal_places=3, max_digits=10, max_length=10)),
                ('uid', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('initial', models.CharField(max_length=10)),
                ('records', models.ManyToManyField(to='piggySQL.record')),
            ],
        ),
    ]
