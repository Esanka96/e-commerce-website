# Generated by Django 4.2.6 on 2023-12-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_lasttable_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lasttable',
            name='photo',
        ),
        migrations.AddField(
            model_name='lasttable',
            name='photourl',
            field=models.CharField(max_length=750, null=True),
        ),
    ]
