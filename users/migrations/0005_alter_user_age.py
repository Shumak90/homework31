# Generated by Django 4.1 on 2022-09-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(),
        ),
    ]
