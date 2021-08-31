from django.urls import reverse
from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    sub_category =models.CharField(max_length=50)
    parent_category= models.ForeignKey('self', limit_choices_to={'parent_category__isnull':True} , on_delete=models.CASCADE, blank=True, null=True)
    
     
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories "
    def __str__(self):
        return str(self.sub_category)
    
class Product(models.Model):
    name=models.CharField(max_length=30, verbose_name='اسم المنتج')
    description=models.TextField(max_length=500, verbose_name ='وصف المنتج')
    img = models.ImageField(upload_to='product', blank=True, null=True , verbose_name ='صوره المنتج')
    price=models.FloatField( verbose_name ='سعر المنتج')
    cost=models.FloatField( verbose_name ='سعر تكلفه المنتج')
    created = models.DateTimeField(auto_now=True)
    category= models.ForeignKey(Category, on_delete=CASCADE , verbose_name ='نوع المنتج')
    discountprice=models.FloatField( verbose_name ='الخصم علي المنتج')
    is_new =models.BooleanField(default=True  , verbose_name ='هل المنتج جديد ؟')
    is_bestseller =models.BooleanField(default=True , verbose_name ='هل المنتج احسن مبيعات ؟')
    slug= models.SlugField(max_length=100,  null=True, blank=True)

    
    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        return reverse("Product:details", kwargs={"slug": self.slug})
    
    
    def __str__ (self):
        return self.name
    


class Product_Alternative(models.Model):
    product_main = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_prodcut' , verbose_name="Product")
    product_alter = models.ManyToManyField(Product , related_name='alternative_products'  , verbose_name="Alternatives")
    
    class Meta:
        verbose_name = "Product Alternative"
        verbose_name_plural = "Product Alternatives"

    def __str__(self):
        return str(self.product_alter)
    
class Product_Accessories(models.Model):
    ACCProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='mainaccessory_prodcut' , verbose_name="Product")
    ACCAlternatives = models.ManyToManyField(Product , related_name='accessories_products' , verbose_name="Accessories")
      
    class Meta:
        verbose_name = "Product Accessory"
        verbose_name_plural = "Product Accessories"
    def __str__(self):
        return str(self.ACCProduct)