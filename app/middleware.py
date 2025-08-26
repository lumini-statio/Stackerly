from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.core.cache import cache
from django.http import HttpResponse
import time


class LoggedInterceptorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        excluded_paths = [
            reverse('login'),
            reverse('signup'),
        ]

        if not request.user.is_authenticated and request.path not in excluded_paths:
            messages.warning(request, "You must be signed up to access that view.")
            return redirect('login')
        
        return self.get_response(request)
    

class RateLimiterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_per_second = 5
        self.cache_timeout = 1
    
    def __call__(self, request):
        ip = self.get_client_ip(request)
        cache_key = f'rl:{ip}'

        count = cache.get(cache_key, 0)

        if count >= self.requests_per_second:
            return HttpResponse('Too many requests. Slow down.', status=429)
        
        cache.incr(cache_key) if cache.get(cache_key) else cache.set(cache_key, 1, timeout=self.cache_timeout)

        response = self.get_response(request)

        return response
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        return ip