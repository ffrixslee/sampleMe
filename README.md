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
> `mysite` is the name of my project

## 4. Testing Setup
```
python manage.py runserver
```

## 5. Set up Django Authentication
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
> `logon` is the name of my Django app

> To create a Django app:

1. cd into `logon` app folder and create a `urls.py`

2. create a `templates` folder and cd into it
    
    1. create a `login.html` file

- app name should be `site_main` instead of `logon`
-------
Issues encountered:
- The issue: In Django 5, LogoutView has been **depreciated**. So, we need to create our view like this:
``` python
@login_required
def user_logout(request):
logout(request)
return render(request, ‘registration/logged_out.html’, {})

In logged_out.html, write the below code.
{% block title %}Logged out{% endblock %}
{% block content %}
```
source: [ https://forum.djangoproject.com/t/showing-method-not-allowed-get-users-logout/26044/8 ]

-------
**Important files to take note of:**
- views.py
- files in templates folder
- urls.py (both in app and project folder)
- settings.py

--------

## Styles
- Originally created a `styles.css` file in `statics/css` folder but opted to use tailwind + flowbite instead

--------
## Miscellaneous
- db.sqlite3 should not be pushed and synchronized
- when working on repo from diff computers, must migrate and create superusers:
```
python manage.py migrate
python manage.py createsuperuser
```
- don't need testProj folder, just directly create app mysite in root folder
- can specify versions to be used in Pipfile
- .env, .env.dist files important for setting django environment variables
- admin.py is where the model files with database schema are stored

--------

#### Windows pc
- For windows pc: use git bash terminal instead of command prompt
- In settings.py: change Time_Zone='Asia/Singapore'

    - If there's an issue with setting timezone, install tzdata:
    
        `pip install tzdata`


