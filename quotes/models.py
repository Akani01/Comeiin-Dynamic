from django.db import models
from products.models import Product


class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('quoted', 'Quoted'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    # Contact info
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    delivery_address = models.TextField(blank=True)
    message = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reference = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.reference:
            super().save(*args, **kwargs)
            self.reference = f"CW-{self.pk:06d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} - {self.name}"


class QuoteItem(models.Model):
    quote = models.ForeignKey(
        QuoteRequest, on_delete=models.CASCADE, related_name='items'
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='quote_items'
    )
    # Snapshot fields (so we always know what was requested)
    product_name = models.CharField(max_length=200)
    product_sku = models.CharField(max_length=80, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.product_name}"