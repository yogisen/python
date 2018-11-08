# Generated by Django 2.1.3 on 2018-11-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(choices=[('android', 'Android'), ('ios', 'iOS')], default='android', max_length=20)),
                ('form_factor', models.CharField(choices=[('phone', 'Phone'), ('tablet', 'Tablet')], default='phone', max_length=20)),
                ('model', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
