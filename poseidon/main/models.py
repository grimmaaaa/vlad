from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    otchestvo = models.CharField('Отчество', max_length=255)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Поситители'


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Entertainment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='entertainments/')
    duration = models.DurationField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Развлечение'
        verbose_name_plural = 'Развлечения'


class Promotion(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='promotions/')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='promotions/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Visit(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    entertainment = models.ForeignKey(Entertainment, on_delete=models.CASCADE, null=True, blank=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.visit_date}"
    
    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'


class Video(models.Model):
    video = models.FileField(upload_to='video/')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
