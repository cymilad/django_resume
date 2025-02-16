from django.db import models


# Create your models here.
class SocailMedia(models.Model):
    telegram = models.URLField(verbose_name='لینک تلگرام')
    youtube = models.URLField(verbose_name='لینک یوتیوب')
    github = models.URLField(verbose_name='لینک گیت هاب')
    instagram = models.URLField(verbose_name='لینک اینستاگرام')

    def __str__(self):
        return 'شبکه های اجتماعی'

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'تنظیمات شبکه های اجتماعی'


class HeroSection(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    job_title = models.CharField(max_length=255, verbose_name='عنوان شغلی')
    button_text = models.CharField(max_length=100, verbose_name='متن دکمه')
    avatar = models.ImageField(upload_to='hero/', verbose_name='تصویر آواتار')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'اطلاعات شخصی'
        verbose_name_plural = 'تنظیمات اطلاعات شخصی'


class Feature(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    svg_code = models.TextField(verbose_name='کد SVG')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'تنظیمات ویژگی ها'


class AboutMe(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=15, verbose_name='شماره موبایل')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    position = models.CharField(max_length=50, verbose_name='سطح')
    freelancer_status = models.BooleanField(default=True, verbose_name='فریلنسر')
    exprience_years = models.PositiveIntegerField(verbose_name='سال های سابقه کار')
    about_title = models.CharField(max_length=150, verbose_name='عنوان درباره من')
    about_description = models.TextField(verbose_name='توضیحات درباره من')
    cv_file = models.FileField(upload_to='cv_file/', verbose_name='فایل رزومه', blank=True, null=True)
    main_image = models.ImageField(upload_to='about/', verbose_name='تصویر اصلی')
    thumb_image = models.ImageField(upload_to='about/thumb', verbose_name='تصویر کوچک', blank=True, null=True)
    ribbon_image = models.ImageField(upload_to='about/ribbon', verbose_name='تصویر نشان', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'تنظیمات درباره من'


class Counter(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    value = models.PositiveIntegerField(verbose_name='مقدار')
    suffix = models.CharField(max_length=100, blank=True, null=True)
    speed = models.IntegerField(default=2000, verbose_name='سرعت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شمارنده'
        verbose_name_plural = 'تنظیمات شمارنده'


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام مهارت')
    percentage = models.PositiveIntegerField(verbose_name='درصد مهارت')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مهارت ها'
        verbose_name_plural = 'تنظیمات مهارت ها'


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    icon = models.TextField(verbose_name='آیکون به صورت SVG')
    order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = 'خدمت'
        verbose_name_plural = 'تنظیمات خدمات'


class WorkExpreience(models.Model):
    position = models.CharField(max_length=100, verbose_name='عنوان شغلی')
    company = models.CharField(max_length=100, verbose_name='اسم شرکت')
    start_year = models.IntegerField(verbose_name='سال شروع فعالیت')
    end_year = models.CharField(max_length=10, blank=True, null=True, verbose_name='سال پایان فعالیت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'تنظیمات سابقه کاری'


class Education(models.Model):
    degree = models.CharField(max_length=100, verbose_name='عنوان رشته')
    univercity = models.CharField(max_length=100, verbose_name='نام دانشگاه')
    start_year = models.IntegerField(verbose_name='سال شروع تحصیل')
    end_year = models.CharField(max_length=10, blank=True, null=True, verbose_name='سال پایانی تحصیل')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.univercity

    class Meta:
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = 'تنظیمات سابقه تحصیلی'


class ProtfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('سایبر آموز', 'CyberAmooz'),
        ('تدریس', 'techear'),
    ]

    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='دسته بندی')
    image_thumbnail = models.ImageField(upload_to='portfolio/thumbanil/', verbose_name='تصویر')
    image_main = models.ImageField(upload_to='portfolio/main/', verbose_name='تصویر اصلی')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'تنظیمات نمونه کار'


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    category = models.CharField(max_length=100, verbose_name='دسته بندی')
    date = models.DateField(verbose_name='تاریخ')
    thumbnail = models.ImageField(upload_to='blog/thumbnails', verbose_name='تصویر')
    main_image = models.ImageField(upload_to='blog/images', verbose_name='تصویر اصلی')
    content = models.TextField(verbose_name='متن مقاله')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست وبلاگ'
        verbose_name_plural = 'مدیریت پست وبلاگ'


class ContactInfo(models.Model):
    address = models.CharField(max_length=255, verbose_name='آدرس')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='تلفن')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'اطلاعات تماس من'
        verbose_name_plural = 'تنظیمات اطلاعات تماس من'


class ContactMessage(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return f'{self.name} - {self.subject}'

    class Meta:
        verbose_name = 'ارتباط با من'
        verbose_name_plural = 'تنظیمات ارتباط با من'
