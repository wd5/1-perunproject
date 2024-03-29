from django.utils import translation


class SubdomainMiddleware:
    """ Make the subdomain publicly available to classes """

    def process_request(self, request):
        domain_parts = request.get_host().split('.')
        if (len(domain_parts) > 2):
            subdomain = domain_parts[0]
            if (subdomain.lower() == 'www'):
                subdomain = None
            domain = '.'.join(domain_parts[1:])
            if subdomain in ('en',):
                translation.activate(subdomain)
                request.LANGUAGE_CODE = translation.get_language()

        else:
            subdomain = None
            domain = request.get_host()
        
        request.subdomain = subdomain
        request.domain = domain
