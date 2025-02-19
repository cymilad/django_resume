# Generated by Django 5.1.6 on 2025-02-15 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_aboutme_cv_file_alter_aboutme_ribbon_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('value', models.PositiveIntegerField()),
                ('suffix', models.CharField(blank=True, max_length=10, null=True)),
                ('speed', models.IntegerField(default=2000)),
            ],
            options={
                'verbose_name': 'شمارنده',
                'verbose_name_plural': 'تنظیمات شمارنده',
            },
        ),
    ]
