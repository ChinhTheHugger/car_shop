from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware

def auth_middleware_ad(get_response):
    # One-time configuration and initialization.

    def middleware_ad(request):
        print(request.session.get('manager'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('manager'):
           return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware_ad