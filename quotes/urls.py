# quotes/urls.py
from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    # API ONLY — the quote is a modal dialog, not a page
    path('api/quotes/', views.QuoteRequestCreateView.as_view(), name='api-quote-create'),
    path('api/quotes/<str:reference>/', views.QuoteRequestDetailView.as_view(), name='api-quote-detail'),
]