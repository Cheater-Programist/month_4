from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255,verbose_name= 'Name')
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name='Message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'