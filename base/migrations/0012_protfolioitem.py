# Generated by Django 5.1.6 on 2025-02-15 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_education_alter_workexpreience_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('category', models.CharField(choices=[('cyberamooz', 'CyberAmooz')], max_length=50, verbose_name='دسته بندی')),
                ('image_thumbnail', models.ImageField(upload_to='portfolio/thumbanil/', verbose_name='تصویر')),
                ('image_main', models.ImageField(upload_to='portfolio/main/', verbose_name='تصویر اصلی')),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'نمونه کار',
                'verbose_name_plural': 'تنظیمات نمونه کار',
            },
        ),
    ]
