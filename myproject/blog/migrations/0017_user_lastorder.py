# Generated by Django 4.2.6 on 2023-12-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_lasttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastorder',
            field=models.ManyToManyField(to='blog.lasttable'),
        ),
    ]