from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(
        source='products.count', read_only=True
    )

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'description',
            'icon_class', 'image', 'order', 'product_count',
        ]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'category_name', 'category_slug',
            'name', 'slug', 'short_description', 'description',
            'sku', 'price', 'image', 'badge',
            'is_featured', 'is_active', 'stock',
            'created_at', 'updated_at',
        ]


class ProductListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list/grid views"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_slug = serializers.CharField(source='category.slug', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'short_description',
            'price', 'image', 'badge',
            'category', 'category_name', 'category_slug',
            'is_featured',
        ]