from django.db import models

# Create your models here.
class InfoUser(models.Model):
    name = models.CharField(
        max_length = 30,
        verbose_name = 'user name'
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Job'
    )
    image = models.ImageField(
        upload_to= 'InfoUser',
        verbose_name= 'Image'
    )
    description = models.TextField(
        verbose_name = 'Description'
    )
    email = models.EmailField(
        verbose_name = 'Email'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'phone number'
    )
    youtube = models.URLField(
        verbose_name = 'YouTube'
    )
    instagram = models.URLField(
        verbose_name = 'Instagram'
    )
    whatsapp = models.URLField(
        verbose_name = 'Whatsapp'
    )
    telegram = models.URLField(
        verbose_name = 'Telegram'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'User admin'
        verbose_name_plural = 'Users admin'