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
    description = models.TextField(verbose_name='توضیحات')
    svg_code = models.TextField(verbose_name='کد SVG')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ویژگی ها'
        verbose_name_plural = 'ویژگی ها'