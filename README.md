# buddha-django
a django site for buddha teachings.

## best practice
https://docs.djangoproject.com/en/1.9/misc/design-philosophies/#dry

## road map
> [click here to begin my work](https://docs.djangoproject.com/en/1.9/intro/tutorial03/)

- [Creating a project](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)
```
django-admin startproject buddha
python manage.py runserver 0.0.0.0:port
```
- Creating a app
```
python manage.py startapp teachings
```
- Write my first view
```
Add view
Create urls.py
Modify urlpatterns
```
- Database setup
```
//creates any necessary database table according to the database in buddha/settings.py
python manage.py migrate
```
- Creating models
```
A model is the single, definitive source of truth about your data. 
It contains the essential fields and behaviors of the data you’re storing. 
Django follows the DRY Principle. 
The goal is to define your data model in one place and automatically derive things from it.
```
- Activating models
```
Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing your objects.
add 'teachings.apps.TeachingsConfig' in settings.py
python manage.py makemigrations teachings
python manage.py sqlmigrate teachings 0001
python manage.py migrate
```
- Three-step guide to making model changes：
```
Change your models(in models.py)
Run 'python manage.py makemigrations' to create migrations for those changes.
Run 'python manage.py migrate' to apply those changes to the database.
```
- Playing with the API
```
Related objects reference: https://docs.djangoproject.com/en/1.9/ref/models/relations/
Field lookups: https://docs.djangoproject.com/en/1.9/topics/db/queries/#field-lookups-intro
Making queries: https://docs.djangoproject.com/en/1.9/topics/db/queries/
```
- Introducing the Django Admin
``` python
# Create a user who can login to the admin site.
python manage.py createsuperuser
# enter username
Username: admin
# enter email address
Email address: xxx@xxx.com
# enter password twice
Password: xxxxx
Password (again): xxxxx
Superuser created successfully
# start server and enter admin site
python manage.py runserver
http://127.0.0.1:8000/admin
```
- ** Make content of teachings modifiable in the admin **
``` python
teachings/admin.py
from django.contrib import admin
from .models import Article
admin.site.register(Article)
```
- Writing more views.
```
To be continue...
```

## Tips
### 1.Three-step guide to making model changes:
```
Change your models(in models.py).
Run 'python manage.py makemigrations' to create migrations for those changes.
Run 'python manage.py migrate' to apply those changes to the database.
```
