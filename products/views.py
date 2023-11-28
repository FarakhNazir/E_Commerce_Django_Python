from django.shortcuts import render
from products.models import Product


# Create your views here.
def get_product(request , slug):
    try:
        product = Product.objects.get(slug = slug)
        if request.GET.get('size'):
            size = request.GET.get('size')
            price =product.price + product.get_product_price_by_size(size)
            print(size)
            print("actual price:", product.price)
            print("after add price:" , price)
            context =  {
                'product' : product,
                'price' : price,
                
            }
           
        return render(request , 'product/product.html', context)
       # product = Product.objects.get(slug =slug)
       # return render(request  , 'product/product.html' , context = {'product' : product})
        #return render(request  , 'product/product.html' )

    except Exception as e:
        print(e)