# core/models.py
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"


class Testimonial(models.Model):
    author = models.CharField(max_length=150)
    role = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.author} - {self.role}"


class Highlight(models.Model):
    """The 'Why Choose Comeiin Works' cards"""
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    icon_class = models.CharField(
        max_length=80,
        help_text="Font Awesome class e.g. 'fas fa-flask'"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class HeroSlide(models.Model):
    image = models.ImageField(upload_to='hero/')
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Slide {self.pk}"