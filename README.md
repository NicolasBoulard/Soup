# Let's start with soup
## For developers
1. Create venv : `python -m venv .venv`
2. Activate venv : `.venv\Script\Activate`
3. Install python requirements : `pip install -r requirements.txt`
4. Set the settings correctly for development:
Define a setting file in the folder soup/settings/dev.py (Content available [here](#settings))
Set the environment variable `DJANGO_SETTINGS_MODULE` to soup.settings.prod if the previous file created is dev.py .
example: `DJANGO_SETTINGS_MODULE=soup.settings.dev`
5. Create database : `python manage.py migrate`
6. Create a super user : `python manage.py createsuperuser --username=admin`
7. Launch debug server : `python manage.py runserver --settings=soup.settings.dev`
## For integrators
Use the docker image available on ghcr.io


### Parameters

## Settings
### Development
```python
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "../../static")
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

### Production
```python
from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "../../static")
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```