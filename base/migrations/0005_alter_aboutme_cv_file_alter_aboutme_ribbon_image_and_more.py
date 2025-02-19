# Generated by Django 5.1.6 on 2025-02-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='cv_file/', verbose_name='فایل رزومه'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='ribbon_image',
            field=models.ImageField(blank=True, null=True, upload_to='about/ribbon', verbose_name='تصویر نشان'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='thumb_image',
            field=models.ImageField(blank=True, null=True, upload_to='about/thumb', verbose_name='تصویر کوچک'),
        ),
    ]
