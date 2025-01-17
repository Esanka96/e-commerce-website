# Generated by Django 4.2.6 on 2023-11-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_posttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postalcode', models.CharField(max_length=20)),
            ],
        ),
    ]
