# products/views.py
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, filters

from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductListSerializer,
)


# ============================================================
# HTML VIEWS
# ============================================================

def catalogue_page(request):
    """Renders catalogue.html — the full product browser."""
    context = {
        'categories': Category.objects.filter(is_active=True),
        'product_count': Product.objects.filter(is_active=True).count(),
    }
    return render(request, 'catalogue.html', context)


def product_detail_page(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'product_detail.html', {'product': product})


# ============================================================
# API VIEWS
# ============================================================

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'short_description', 'description', 'sku']
    ordering_fields = ['name', 'price', 'created_at']

    def get_queryset(self):
        qs = Product.objects.filter(is_active=True).select_related('category')
        category = self.request.query_params.get('category')
        featured = self.request.query_params.get('featured')

        if category:
            qs = qs.filter(category__slug=category)
        if featured == 'true':
            qs = qs.filter(is_featured=True)
        return qs


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_field = 'slug'