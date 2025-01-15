from django.db import models

# Create your models here.
class Head_page(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(blank=True)
    time_create=models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now_add=True)
    public=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Ифориация на главной странице"
        verbose_name = "Последние посты"

class About_page(models.Model):
    about_title=models.CharField(max_length=200)
    about_content=models.TextField(blank=True)
    about_time_create=models.DateTimeField(auto_now=True)
    about_time_update = models.DateTimeField(auto_now_add=True)
    about_public=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Портфолио"
        verbose_name = "Последние посты"

class Contact_page(models.Model):
    contact_title = models.CharField(max_length=200)
    contact_content=models.TextField(blank=True)
    contact_time_create=models.DateTimeField(auto_now=True)
    contact_time_update = models.DateTimeField(auto_now_add=True)
    contact_public=models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "обратная связь"
        verbose_name = "Последние посты"
