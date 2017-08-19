##DJango admin 

In this we will use DJango admin to maintenance add, edit and delete news content
with register class News on admin.py file.

1. Go to on Command Prompt type _cd Django01_
2. Open admin.py file in \Django\blog then add and save the following script :
```python
from django.contrib import admin
from .models import News

admin.site.register(News)
``` 
3. Activate virtual environment with type _myvenv\Scripts\activate_
4. Type _python manage.py createsuperuser_ for create user and password at DJango admin.
5. Run webapp with type _python manage.py runserver_
6. Open browser type localhost:8000\admin on url.
7. Login with superuser which we was create.
