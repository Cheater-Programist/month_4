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
        return self.name            #Будет называться каждая моделька в админ панеле

    class Meta:
        verbose_name = 'User admin'
        verbose_name_plural = 'Users admin'

class Numbers(models.Model):
    experience = models.IntegerField(
        verbose_name = 'experience'
    )
    project = models.IntegerField(
        verbose_name = 'projects'
    )
    clientes = models.IntegerField(
        verbose_name = 'customers'
    )

    def __str__(self) -> str:
        return f"Experience: {self.experience}, Projects: {self.project}, Customers: {self.clientes}"
    
    class Meta:
        verbose_name = "Number"
        verbose_name_plural = "Numbers"


class Service(models.Model):
    number = models.IntegerField(verbose_name = 'ID')
    title = models.CharField(max_length = 255, verbose_name = 'Title')
    description = models.TextField(verbose_name = 'Description')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Experience(models.Model):
    year = models.CharField(max_length = 255, verbose_name = 'Year')
    title = models.CharField(max_length = 255, verbose_name = 'Title')
    subtitle = models.CharField(max_length = 255, verbose_name = 'SubTitle')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

class Educations(models.Model):
    year = models.CharField(max_length = 255, verbose_name = 'Year')
    title = models.CharField(max_length = 255, verbose_name = 'Title')
    subtitle = models.CharField(max_length = 255, verbose_name = 'SubTitle')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

class Skills(models.Model):
    image = models.ImageField(upload_to='skills', verbose_name='Image')
    pronc = models.IntegerField(verbose_name = "Percent")
    title = models.CharField(max_length = 255, verbose_name = "Title")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"