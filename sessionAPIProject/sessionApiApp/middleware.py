from django.http import HttpResponse

class MiddlewareLifeCycle:
    def __init__(self, get_response):
        print('init envoked')
        self.get_response = get_response
    
    def __call__(self, request):
        print('Before View is executed')
        response = self.get_response(request)
        print('After View is executed')
        return response

class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        print(exception.__class__.__name__)
        return HttpResponse('<strong>Currently facing issues check back later</strong>')
