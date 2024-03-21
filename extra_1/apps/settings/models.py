from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка 1'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка 2'
    )
    descriptions2 = models.TextField(
        verbose_name = 'Описание 2'
    )       
    title3 = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка 3'
    )
    descriptions3 = models.TextField(
        verbose_name = 'Описание 3'
    )
    title4 = models.CharField(
        max_length=155,
        verbose_name = 'Заголовка 4'
    )
    descriptions4 = models.TextField(
        verbose_name = 'Описание 4'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройки всего страницы'