# Generated by Django 5.0.6 on 2024-06-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, default='fallback.png', upload_to='')),
            ],
        ),
    ]