# Generated by Django 4.2.4 on 2023-08-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
