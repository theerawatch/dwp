from django.shortcuts import redirect
class AuthenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.included_urls = ['/a/','/u/']  # Add any excluded URLs here
    
    def __call__(self, request):
        # Check if the current request URL is included
        if any(request.path.startswith(url) for url in self.included_urls):
            if not request.session.get('email'):
                return redirect('/login/')
        
        response = self.get_response(request)
        return response