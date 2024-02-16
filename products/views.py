from django.shortcuts import render
from django.db.models import Q
from .models import Product, CATEGORY_CHOICES
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import Product, Cart, CartItem
def product_list(request):
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', '')
    
    products = Product.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category:
        products = products.filter(category=category)

    if sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'price_asc':
        products = products.order_by('price')

    paginator = Paginator(products, 16)  # Serve 16 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': page_obj,
        'CATEGORY_CHOICES': CATEGORY_CHOICES
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    
    # Assuming cart.items.all() gives you all cart items for the user
    cart_items_count = cart.items.count()
    return JsonResponse({'cartItemsCount': cart_items_count})

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})

# views.py
@login_required
def cart_items(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'products/cart_items.html', {'cart': cart})