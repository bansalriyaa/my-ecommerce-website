# store/urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView, like_product
from .views import search_results

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', search_results, name='search_results'),
    path('like/<int:product_id>/', like_product, name='like_product'),
    # Add more URLs as needed
]
