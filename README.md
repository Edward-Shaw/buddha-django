# buddha-django
a django site for buddha teachings.

## where to begin
https://docs.djangoproject.com/en/1.9/intro/tutorial02/

## best practice
https://docs.djangoproject.com/en/1.9/misc/design-philosophies/#dry

## Tips
### 1.Three-step guide to making model changes:
``` python
change your models(in models.py).
Run 'python manage.py makemigrations' to create migrations for those changes.
Run 'python manage.py migrate' to apply those changes to the database.
```
