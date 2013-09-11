from django.db import models
from extimagefield import ExtImageField


class ProductCategory(models.Model):
    title_en=models.CharField(max_length=200, verbose_name='Название (EN)')
    title_ru=models.CharField(max_length=200, verbose_name='Название (RU)')
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique", verbose_name='Слаг')
    def get_absolute_url(self):
        return "/products/%s/" % self.slug    
    def __unicode__(self):
        return self.title_ru
    class Meta:
        verbose_name = "Категория продукта"
        verbose_name_plural = "Категории продуктов"        


class DecorationCategory(models.Model):
    title_en=models.CharField(max_length=200, verbose_name='Название (EN)')
    title_ru=models.CharField(max_length=200, verbose_name='Название (RU)')
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique", verbose_name='Слаг')
    def get_absolute_url(self):
        return "/decorations/%s/" % self.slug
    def __unicode__(self):
        return self.title_ru
    class Meta:
        verbose_name = "Категория оформления"
        verbose_name_plural = "Категории оформления"                


class DecorationIngredient(models.Model):
    title_en=models.CharField(max_length=200, verbose_name='Название (EN)')
    title_ru=models.CharField(max_length=200, verbose_name='Название (RU)')
    descr_en=models.TextField(verbose_name='описание состава (ΕΝ)')
    descr_ru=models.TextField(verbose_name='описание состава (RU)')
    def __unicode__(self):
        return self.title_ru
    class Meta:
        verbose_name = "Состав торта"
        verbose_name_plural = "Составы тортов"        


class Product(models.Model):
    title_en = models.CharField(max_length=200, verbose_name='Название (EN)')
    title_ru=models.CharField(max_length=200, verbose_name='Название (RU)')
    descr_en=models.TextField(verbose_name='описание (ΕΝ)')
    descr_ru=models.TextField( verbose_name='описание (RU)')
    productCategory=models.ForeignKey(ProductCategory, verbose_name='Категория')
    photo = ExtImageField(upload_to='photos', sizes=((125,125),), verbose_name='Фото', max_size=(850, 590), watermark="DELIKAT")
    def __unicode__(self):
        return self.title_ru
    def photo_admin_thumbnail(self):
        return "<img src='"+self.photo.url_125x125+"'/>"
    photo_admin_thumbnail.allow_tags = True       
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продуты"        


class Decoration(models.Model):
    code = models.CharField(max_length=200, verbose_name='Код')
    decorationCategory=models.ManyToManyField(DecorationCategory, verbose_name='Категории')
    descr_en=models.TextField(verbose_name='описание (ΕΝ)')
    descr_ru=models.TextField(verbose_name='описание (RU)')
    photo = ExtImageField(upload_to='photos', sizes=((125,125),), verbose_name='Фото', max_size=(850, 590), watermark="DELIKAT")    
    def __unicode__(self):
        return self.code
    def photo_admin_thumbnail(self):
        return "<img src='"+self.photo.url_125x125+"'/>"
    photo_admin_thumbnail.allow_tags = True
    def categories_admin(self):
        ls=self.decorationCategory.all()
        res="N/D"
        if ls :
            res="<ul>"
            for o in ls:
                res+="<li>"+str(o)+"</li>"
            res+="</ul>"
        return res
    categories_admin.allow_tags = True
    class Meta:
        verbose_name = "Оформление"
        verbose_name_plural = "Оформления"

