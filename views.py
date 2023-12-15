
# store/views.py
from urllib.parse import quote_from_bytes
from django.views.generic import ListView, DetailView
from .models import Product
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

def search_results(request):
    query = request.GET.get('query', '')
    results = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'query': query,'results': results})

def like_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.likes += 1
    product.save()
    return JsonResponse({'likes': product.likes})