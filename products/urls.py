# products/urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # ✅ API FIRST — so `/products/api/...` matches before `<slug>/`
    path('api/categories/', views.CategoryListView.as_view(), name='api-categories'),
    path('api/products/', views.ProductListView.as_view(), name='api-products'),
    path('api/products/<slug:slug>/', views.ProductDetailView.as_view(), name='api-product-detail'),

    # Pages
    path('', views.catalogue_page, name='catalogue'),              # /products/
    path('<slug:slug>/', views.product_detail_page, name='product-detail'),  # /products/microscopes-imaging/
]