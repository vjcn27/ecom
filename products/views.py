from django.shortcuts import render
from products.models import Product

# Create your views here.
def get_product(request, slug):
    try:

        product = Product.objects.get(slug=slug)
        context={'product':product}
        if request.GET.get('size'):
            size=request.GET.get('size')
            price=Product.get_product_by_size(size)
            context['selected_size']=size
            context['updated_price']=price
            print(price)

        return render(request, "product/product.html",context={'product':product })
    except Exception as e:
        print(e)    