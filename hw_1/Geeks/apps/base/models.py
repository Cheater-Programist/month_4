from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'user name')
    lastname = models.CharField(max_length = 255, verbose_name = 'user surname')
    job = models.CharField(max_length = 255, verbose_name = 'user job')
    image = models.ImageField(upload_to='UserInfo', verbose_name= 'user image')
    description = models.TextField(verbose_name = 'user description')
    age = models.IntegerField(verbose_name = 'user age')
    email = models.EmailField(verbose_name = 'user email')
    adsress = models.CharField(max_length = 255, verbose_name = 'user address')
    youtube = models.URLField(verbose_name = 'YouTube')
    instagram = models.URLField(verbose_name = 'Instagram')
    whatsapp = models.URLField(verbose_name = 'Whatsapp')
    telegram = models.URLField(verbose_name = 'Telegram')
    facebook = models.URLField(verbose_name = 'Facebook')

    def __str__(self) -> str:
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = 'User admin'
        verbose_name_plural = 'Users admin'