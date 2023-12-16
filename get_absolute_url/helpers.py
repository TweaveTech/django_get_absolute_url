from django.conf import settings
from django.urls import reverse_lazy as django_reverse_lazy
import socket

def get_schema():
    try:
        if settings.HTTPS_SUPPORTED:
            schema = 'https'
        else:
            schema = 'http'
    except AttributeError:
        schema = 'http'

    return schema


def get_fqdn():
    hostname = socket.getfqdn()

    try:
        if settings.DEBUG and settings.LOCAL_HOST:
            hostname = settings.LOCAL_HOST
    except AttributeError:
        pass

    return hostname


def generate_absolute_url(trailing_slash=True, reverse_url_string=None):
    '''
    Return a complete URL for the server. Usefuel when you need links 
    in emails, sms, telegram or whatsapp messages.

    There are 2 settings needed in your settings.
    - HTTPS_SUPPORTED (boolean) -> Will ensure the url starts with the correct schema.
    - LOCAL_HOST(hostname/ip) -> Will be used if present and debug is active to override
    the local hostname detected by socket.getfqdn()

    '''
    schema = get_schema()
    hostname = get_fqdn()

    url = f"{schema}://{hostname}"

    if trailing_slash:
        url = url + '/'

    if reverse_url_string:
        uri = django_reverse_lazy(reverse_url_string)
        return url.rstrip('/') + uri

    return url


def get_absolute_media_url(trailing_slash=True):
    """
    Return a complete media url
    """
    url = generate_absolute_url(trailing_slash=False)
    media_uri = settings.MEDIA_URL

    url = url + media_uri

    if not trailing_slash:
        url = url.rstrip('/')

    return url

    
def get_absolute_static_url(trailing_slash=True):
    """
    Return a complete media url
    """
    url = generate_absolute_url(trailing_slash=False)
    media_uri = settings.STATIC_URL

    if not trailing_slash:
        url = url.rstrip('/')

    return url + media_uri



def reverse_lazy(viewname, urlconf=None, args=None, kwargs=None, current_app=None):
    '''
    Return a complete URL for the server. Usefuel when you need links 
    in emails, sms, telegram or whatsapp messages.

    There are 2 settings needed in your settings.
    - HTTPS_SUPPORTED (boolean) -> Will ensure the url starts with the correct schema.
    - LOCAL_HOST(hostname/ip) -> Will be used if present and debug is active to override
    the local hostname detected by socket.getfqdn()

    '''
    base_url = generate_absolute_url(trailing_slash=False)
    uri = django_reverse_lazy(viewname, urlconf=urlconf, args=args, kwargs=kwargs,
        current_app=current_app)

    return base_url + uri





    
