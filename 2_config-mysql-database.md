# Config MySQL in DJango

1. Open Command Prompt then login to your mysql.
2. Create database with name is djangodb(sample for me).
3. Go to django project folder with type (cd Django) on command Prompt.
4. Open Setting file with your editor then copy the following script :

	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'your database',
        'USER': 'your user',
        'PASSWORD': 'your password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
		}
	}
  
5. Activate virtual environment with type (mynenv\Scripts\activate).
6. Install mysqlclient package with type (pip install django mysqlclient).
7. Type (python manage.py migrate).
8. Go to your mysql then type (show tables;). Configuration tables will be created automaticaly there.