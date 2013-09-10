from models import *
from forms import *
from django.db.models import get_model
from django.contrib import admin

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title_en'] }
    
class DecorationCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title_en'] }    
    
class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
            'photo': AdminImageWidget(),
        } 
        
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_ru',  'productCategory', 'photo_admin_thumbnail')
    list_display_links = ('title_ru', 'photo_admin_thumbnail')
    search_fields = ('title_ru',)
    list_filter = ['productCategory']
    form = ProductAdminForm
    
  

class DecorationAdminForm(ModelForm):
    class Meta:
        model = Decoration
        widgets = {
            'photo': AdminImageWidget(),
        }   
        
class DecorationAdmin(admin.ModelAdmin):
    list_display = ('code',  'categories_admin', 'photo_admin_thumbnail')
    list_display_links = ('code', 'photo_admin_thumbnail')
    search_fields = ('code',)
    list_filter = ['decorationCategory']
    form = DecorationAdminForm
    


        
    

    
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(DecorationCategory, DecorationCategoryAdmin)
admin.site.register(DecorationIngredient)
admin.site.register(Product, ProductAdmin)
admin.site.register(Decoration, DecorationAdmin)
#admin.site.register(get_model('myproject', 'Decoration'), DecorationAdmin)