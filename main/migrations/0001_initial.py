# Generated by Django 5.0.7 on 2024-07-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='email@gmail.com', max_length=254, null=True)),
                ('subject', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
