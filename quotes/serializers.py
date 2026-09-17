from rest_framework import serializers
from .models import QuoteRequest, QuoteItem


class QuoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteItem
        fields = [
            'id', 'product', 'product_name',
            'product_sku', 'quantity', 'notes',
        ]
        extra_kwargs = {
            'product_name': {'required': False},
        }

    def validate(self, attrs):
        # Auto-fill product_name/sku if product is given but name not
        product = attrs.get('product')
        if product and not attrs.get('product_name'):
            attrs['product_name'] = product.name
            attrs['product_sku'] = product.sku or ''
        if not attrs.get('product_name') and not product:
            raise serializers.ValidationError(
                "Either 'product' or 'product_name' is required."
            )
        return attrs


class QuoteRequestSerializer(serializers.ModelSerializer):
    items = QuoteItemSerializer(many=True)

    class Meta:
        model = QuoteRequest
        fields = [
            'id', 'reference', 'name', 'email', 'phone',
            'company', 'delivery_address', 'message',
            'status', 'created_at', 'items',
        ]
        read_only_fields = ['id', 'reference', 'status', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        quote = QuoteRequest.objects.create(**validated_data)
        for item_data in items_data:
            QuoteItem.objects.create(quote=quote, **item_data)
        return quote