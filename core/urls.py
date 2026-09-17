# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # HTML pages
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('privacy/', views.privacy_view, name='privacy'),

    # API
    path('api/contact/', views.ContactMessageCreateView.as_view(), name='api-contact'),
    path('api/testimonials/', views.TestimonialListView.as_view(), name='api-testimonials'),
    path('api/highlights/', views.HighlightListView.as_view(), name='api-highlights'),
    path('api/hero-slides/', views.HeroSlideListView.as_view(), name='api-hero-slides'),

    # PWA
    path('manifest.json', views.pwa_manifest, name='pwa-manifest'),
    path('serviceworker.js', views.pwa_sw, name='pwa-sw'),
]