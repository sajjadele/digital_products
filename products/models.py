from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE )
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar') , blank=True , upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update_time') , auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name =_('Category')
        verbose_name_plural = __name__('Categories')



class Products(models.Model):
    



    
