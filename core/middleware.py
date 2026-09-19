# core/middleware.py
from django.http import HttpResponsePermanentRedirect

# Map legacy .html paths to new Django URLs
LEGACY_MAP = {
    '/index.html':     '/',
    '/about.html':     '/about/',
    '/privacy.html':   '/privacy/',
    '/contact.html':   '/#contact',      # note: fragment is client-side
    '/catalogue.html': '/products/',
    '/laboratory.html':'/laboratory/',
    '/engineering.html':'/engineering/',
}

class LegacyHtmlRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        # Strip trailing slash variations
        target = LEGACY_MAP.get(path) or LEGACY_MAP.get(path.rstrip('/') + '/')
        if target:
            # Preserve query string
            qs = request.META.get('QUERY_STRING', '')
            if qs:
                # Careful with fragments — query goes before #
                if '#' in target:
                    base, frag = target.split('#', 1)
                    target = f'{base}?{qs}#{frag}'
                else:
                    target = f'{target}?{qs}'
            return HttpResponsePermanentRedirect(target)
        return self.get_response(request)