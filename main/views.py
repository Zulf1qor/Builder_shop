from django.shortcuts import render

def index_view(request):
    context = {

    }
    return render(request, 'index.html', context)

def about_view(request):
    context ={

    }
    return render(request, 'about.html', context)

def shop_view(request):
    context={

    }
    return render(request, 'shop.html', context)

def product_view(request):
    context={

    }
    return render(request, 'product.html', context)


def cart_view(request):
    context={

    }
    return render(request, 'cart.html', context)

def checkout_view(request):
    context={

    }
    return render(request, 'checkout.html', context)

def wishlist_view(request):
    context={

    }
    return render(request, 'wishlist.html', context)

def blog_view(request):
    context={

    }
    return render(request, 'blog.html', context)

def blogdetails_view(request):
    context={

    }
    return render(request, 'wishlist.html', context)


def contact_view(request):
    context={

    }
    return render(request, 'contact.html', context)
