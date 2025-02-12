# Project initialization
## 1. Create a Github repo
> Take note of the .gitignore and initialize with a Readme file

## 2. Create a local project folder
```
% mkdir testProj
% cd testProj
```

## 3. Create and activate a virtual environment

<br>Option 1: Using pipenv
```
% pip install pipenv (if haven't done so alr)
% pipenv install django
% pipenv shell
```

<br>Option 2: Using venv
```
% python -m venv env

On Windows:
% .\env\Scripts\activate

On Mac/Linux:
% source env/bin/activate
```

> Use pipenv if you like having dependency management combined with virtual environment creation. It simplifies things by automatically tracking packages in Pipfile.

> Use venv if you want a lighter, more basic setup or if you're working on a project that already uses requirements.txt.

## 3. Create a Django project
```
django-admin startproject mysite 
```

## 4. Testing Setup
```
python manage.py runserver
```

# Django-specific

```
python manage.py startapp logOn 
```

## 1. Set up Django Authentication
> Create a Superuser for Testing

*(IMPORTANT)*
```
python manage.py migrate 
```
Must run migrations for the following reasons:

> ✅ To create necessary tables for Django’s built-in authentication system

> ✅ Sets up the auth_user table where users will be stored

> ✅ Ensures everything is synced with the database

<br>


```
python manage.py createsuperuser
```
> You will be prompted for a username, email and password

```
python manage.py startapp logOn 
```
> To create a Django app

> cd into the app and create a `template` folder and cd into it

> create a `login.html` in templates folder

> create a `urls.py` in one folder up


Issues encountered:
- The issue: In Django 5, LogoutView has been depreciated. So, we need to create our view like this:
``` python
@login_required
def user_logout(request):
logout(request)
return render(request, ‘registration/logged_out.html’, {})

In logged_out.html, write the below code.
{% block title %}Logged out{% endblock %}
{% block content %}
```
source: https://forum.djangoproject.com/t/showing-method-not-allowed-get-users-logout/26044/8

-------
**Important files to take note of:**
- views.py
- files in templates folder
- urls.py (both in app and project folder)
- settings.py

--------