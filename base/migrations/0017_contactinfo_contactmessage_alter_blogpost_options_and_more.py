# Generated by Django 5.1.6 on 2025-02-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='آدرس')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
            ],
            options={
                'verbose_name': 'اطلاعات تماس من',
                'verbose_name_plural': 'تنظیمات اطلاعات تماس من',
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('subject', models.CharField(max_length=200, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='پیام')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
            ],
            options={
                'verbose_name': 'ارتباط با من',
                'verbose_name_plural': 'تنظیمات ارتباط با من',
            },
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'پست وبلاگ', 'verbose_name_plural': 'مدیریت پست وبلاگ'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
    ]
