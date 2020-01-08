from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):

    if request.method == "POST":
        #add some form field validation here if required
        product = Product()
        product.title = request.POST['title']
        product.body = request.POST['summary']
        product.url = request.POST['url']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.hunter = request.user
        product.save()
        return render(request, 'products/create.html', {'message':'Product has been added'})
    else:
        return render(request, 'products/create.html')