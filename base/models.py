from django.db import models


# Create your models here.
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
        verbose_name_plural = 'اطلاعات شخصی'


class Feature(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.CharField(max_length=300, verbose_name='توضیحات')
    svg_code = models.TextField(verbose_name='کد SVG')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'


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
    title = models.CharField(max_length=100,verbose_name='عنوان')
    value = models.PositiveIntegerField(verbose_name='مقدار')
    suffix = models.CharField(max_length=10, blank=True, null=True)
    speed = models.IntegerField(default=2000,verbose_name='سرعت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شمارنده'
        verbose_name_plural = 'تنظیمات شمارنده'
