# Generated by Django 5.1.6 on 2025-02-15 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_skill_alter_counter_speed_alter_counter_suffix_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='title',
        ),
    ]
