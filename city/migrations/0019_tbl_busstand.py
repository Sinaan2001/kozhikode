# Generated by Django 3.2.9 on 2022-09-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0018_rename_taxi_name_tbl_taxistand_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_busstand',
            fields=[
                ('Busstand_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=90)),
                ('Category', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'tbl_busstand',
            },
        ),
    ]
