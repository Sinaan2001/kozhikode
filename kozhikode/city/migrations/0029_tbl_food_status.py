# Generated by Django 3.2.9 on 2022-09-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0028_id_gen_review_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_food',
            name='Status',
            field=models.CharField(default='s', max_length=90),
            preserve_default=False,
        ),
    ]
