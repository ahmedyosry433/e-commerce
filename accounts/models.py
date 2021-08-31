from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.text import slugify
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Customer (models.Model):
    user= models.OneToOneField(User , on_delete=models.CASCADE , verbose_name='المستخدم')
    img = models.ImageField(upload_to= 'Customer_image', blank=True, null=True, verbose_name='الصوره')
    country= CountryField( verbose_name='الدوله')
    address = models.CharField(max_length=100, verbose_name='العنوان')
    join_date= models.DateTimeField(default=datetime.datetime.now, verbose_name='تاريخ الانضمام')
    slug = models.SlugField(blank=True, null=True)
    
    def save (self, *args ,**kwargs):
        if not self.slug :
            self.slug= slugify(self.user.username)
        super(Customer , self). save(*args, **kwargs)
        
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)




    
    