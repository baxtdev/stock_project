from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('Stock'))
    description = models.TextField(_('Description'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Created'))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_('Updated'))
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")      


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('Category'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=_('Category'))
    name = models.CharField(max_length=100,verbose_name=_('Product'))
    description = models.TextField(_('Description'))
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name=_('Price'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Created'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ['-created_at']


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=_('Product'),related_name="photos")
    image = models.ImageField(verbose_name=_('Image'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Created'))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_('Updated'))
    
    def __str__(self) -> str:
        return self.product.name
    
    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")
        ordering = ['-created_at']
