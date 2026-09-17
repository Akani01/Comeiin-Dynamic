# quotes/views.py
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.response import Response

from .models import QuoteRequest
from .serializers import QuoteRequestSerializer


# ---------- API ----------

class QuoteRequestCreateView(generics.CreateAPIView):
    """POST /quote/api/quotes/ — submit quote/order enquiry"""
    queryset = QuoteRequest.objects.all()
    serializer_class = QuoteRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quote = serializer.save()

        try:
            items_txt = "\n".join(
                f"- {i.quantity}x {i.product_name} ({i.product_sku})"
                for i in quote.items.all()
            )
            send_mail(
                subject=f"New Quote Request {quote.reference}",
                message=(
                    f"Reference: {quote.reference}\n"
                    f"Name: {quote.name}\n"
                    f"Email: {quote.email}\n"
                    f"Phone: {quote.phone}\n"
                    f"Company: {quote.company}\n"
                    f"Address: {quote.delivery_address}\n\n"
                    f"Items:\n{items_txt}\n\n"
                    f"Message:\n{quote.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass

        return Response(
            {
                'success': True,
                'reference': quote.reference,
                'message': 'Quote request submitted successfully.',
            },
            status=status.HTTP_201_CREATED,
        )


class QuoteRequestDetailView(generics.RetrieveAPIView):
    queryset = QuoteRequest.objects.prefetch_related('items')
    serializer_class = QuoteRequestSerializer
    lookup_field = 'reference'