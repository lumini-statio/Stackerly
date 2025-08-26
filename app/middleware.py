from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse


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