# Generated by Django 5.2.1 on 2025-05-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField(blank=True)),
                ('name', models.CharField(blank=True, max_length=80)),
                ('category', models.CharField(blank=True, max_length=80)),
                ('price', models.IntegerField(blank=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='photos/')),
            ],
        ),
    ]
