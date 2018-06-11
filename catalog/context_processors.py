from .models import Category

def categories(req):
    return {
        'categories': Category.objects.all()
    }
