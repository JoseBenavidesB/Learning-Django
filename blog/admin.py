from django.contrib import admin
from .models import Category, Article
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'update_at')
    search_fields = ('title', 'content', 'user__username', 'catogories__name') #el __username es para acceder al propiedad del modelo
    list_display = ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'user__username','catogories__name')

    def save_model(self, request, obj, form, change): #esto es para guardar el nombre usuario que crea el articulo
        if not obj.user_id: 
            obj.user_id = request.user.id

        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)