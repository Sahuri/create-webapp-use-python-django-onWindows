## Installing DJango-Bower for manage javascript library.

1. Go to on Command Prompt type _cd Django01_. 
2. Activate virtual environment _myvenv\SCripts\activate.
3. Copy the following script to install nodejs for install bower use npm.
```python
pip install nodeenv
pip install django-bower
nodeenv --prebuilt -p
npm install -g bower
```
4. Add django-bower to INSTALLED_APPS in your settings.py in \Django01\mysite folder :
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'djangobower',
]
```
5. Add staticfinder to STATICFILES_FINDERS, specify path to bower components root and bower installed apps :
```python
STATICFILES_FINDERS=(
    'djangobower.finders.BowerFinder',)
	
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'assets')

BOWER_INSTALLED_APPS = (
    'jquery',
)
```
6. To install package you can type _python manage.py bower install_ then enter.
7. To find packages in bower you can type _python manage.py bower seach <package name>_.
8. You must run _python manage.py bower install_ every time you add package. 
