# Generated by Django 4.2.6 on 2023-12-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_maintable_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintable',
            name='sname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]