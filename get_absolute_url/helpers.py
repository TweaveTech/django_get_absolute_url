from django.conf import settings
from django.urls import reverse_lazy
import socket

def schema():
    try:
        if settings.HTTPS_SUPPORTED:
            schema = 'https'
        else:
            schema = 'http'
    except AttributeError:
        schema = 'http'

    return schema


def fqdn():
    hostname = socket.getfqdn()

    if settings.DEBUG:
        try:
            if settings.LOCAL_HOST:
                hostname = settings.LOCAL_HOST
            else:
                raise AttributeError
        except AttributeError:
            hostname = socket.getfqdn()

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
    schema = schema()
    hostname = fqdn()

    url = f"{schema}://{hostname}"

    if trailing_slash:
        url = url + '/'

    if reverse_url_string:
        uri = reverse_lazy(reverse_url_string)
        return url.rstrip('/') + uri

    return url


def get_absolute_media_url(trailing_slash=True):
    """
    Return a complete media url
    """
    url = generate_absolute_url(trailing_slash=True)
    media_uri = settings.MEDIA_URL

    return url + media_uri

    
def get_absolute_static_url(trailing_slash=True):
    """
    Return a complete media url
    """
    url = generate_absolute_url(trailing_slash=True)
    media_uri = settings.STATIC_URL

    return url + media_uri

    
