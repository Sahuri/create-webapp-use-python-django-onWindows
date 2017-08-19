## Config MySQL in DJango

1. Open Command Prompt then login to your mysql.
2. Create database with name is djangodb(sample for me).
3. Go to django project folder with type _cd Django01_ on command Prompt.
4. Open Setting file with your editor then copy the following script :
```python
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
```  
5. Activate virtual environment with type _myvenv\Scripts\activate_.
6. Install mysqlclient package with type _pip install django mysqlclient_.
7. Type _python manage.py migrate_.
8. Go to your mysql then type (show tables;). Configuration tables will be created automaticaly there.
