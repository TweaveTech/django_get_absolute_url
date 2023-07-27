# django_get_absolute_url
A simple helper function to generate absolute urls 

## Quickstart

1. Install the app via the git-url
2. add `get_absolute_url` to the installed apps
3. Add the following settings to your django settings file:

  - `HTTPS_SUPPORTED` (Boolean)
  - `LOCAL_HOST` (url or ip)

4. Whenever you want to generate a url: `from get_absolute_url.helpers import generate_absolute_url`