from blog.models import Category, Article

def get_categories(request):

    categories_in_use = Article.objects.filter(public=True).values_list('catogories', flat=True) #sacar id categories que se usan

    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name') #mostrar solo categories que se usan, las subconsultas
    #se hacen con el guion bajo guion bajo in: por ejemplo id__in saque los id en
    return {
        'categories_from_processor_blog': categories,
        
    }