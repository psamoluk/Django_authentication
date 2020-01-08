from django.shortcuts import render, redirect, get_object_or_404
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
        # return render(request, 'products/create.html', {'message':'Product has been added'})
        return redirect('/products/product/' + str(product.id))
    else:
        return render(request, 'products/create.html')

def product(request, product_id):
    # product = Product.objects.filter(id=product_id)
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/product/' + str(product.id))
    else:
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'products/product.html',{'product':product})