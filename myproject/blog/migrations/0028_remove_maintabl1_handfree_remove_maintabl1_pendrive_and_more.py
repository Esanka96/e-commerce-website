# Generated by Django 4.2.6 on 2023-12-29 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_totaltable_avreview_totaltable_recount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintabl1',
            name='handfree',
        ),
        migrations.RemoveField(
            model_name='maintabl1',
            name='pendrive',
        ),
        migrations.RemoveField(
            model_name='maintabl1',
            name='powerbank',
        ),
        migrations.RemoveField(
            model_name='maintable',
            name='handfree',
        ),
        migrations.RemoveField(
            model_name='maintable',
            name='pendrive',
        ),
        migrations.RemoveField(
            model_name='maintable',
            name='powerbank',
        ),
        migrations.DeleteModel(
            name='postTable',
        ),
        migrations.DeleteModel(
            name='Handfree',
        ),
        migrations.DeleteModel(
            name='Maintabl1',
        ),
        migrations.DeleteModel(
            name='Maintable',
        ),
        migrations.DeleteModel(
            name='Pendrive',
        ),
        migrations.DeleteModel(
            name='Powerbank',
        ),
    ]