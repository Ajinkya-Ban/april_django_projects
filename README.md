Django
-------------------
Q. What is django?
Q. What are the different advantages of django?
Q. How you can install django in windows os?
Q. How you can make the django first project.

Installation step:
--------------------
1. Official website for django https://www.djangoproject.com/ on this website you can download the official document of django.

2. For starting the django first you need to install python.

3. Then You need to install django for creating the web applications by using command on command prompt
	pip install django

4. The above command install latest version of django on your system(5.0.6).

Q. After installing django check the latest version using the below code on command prompt
	C:\Users\hp>python
	Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import django
	>>> print(django.get_version())
		5.0.6

Q. How you can create the first django project?
----------------------
1. Create the folder on any drive like (C: or D:)
2. In that folder create django project using the command as below
	django-admin startproject project1
		OR
	python -m django startproject project1

3. In one project there should be multiple applications.

4. To create the application we use the command on command prompt, first you need to go into project folder
	E:\Django_projects>cd project1
	E:\Django_projects\project1>python manage.py startapp myapp
	
5. After executing the above command your application is ready.

6. In your project folder there are two folder created,
	a) project folder
	b) myapp folder


7. In project level folder there are some files,
	a) __init__.py  : This file told to django that it is python package.
	b) asgi.py: asynchronous gateway interface this file will be used in when you perform deployment. 
	c) settings.py(imp) : This file help us to do setting with application, database setting, template setting.
				      here the template is html / css / bootstrap/ javascript.
	d) urls.py(imp) : This file contains the endpoint. 
		For example:
		--------------------
			https://127.0.0.1:8000/hello
			
	e) wsgi.py: Webserver gateway interface, this file also used for to host your project on server that					 deployment.
	
	f) manage.py(imp) : The manage.py file can be used for to manage all project level settings. This file can be used for below operations,
		1. To run your application we can use the manage.py
			python manage.py runserver
		2. To create the application we can use the manage.py
			python manage.py startapp myapp
		3. To create the models(database) we can also use manage.py file.
		

8. In application level there are some files,
	a)__init__.py
	b) admin.py
	c) apps.py
	d) models.py
	e) views.py(imp) : In django views.py file contains bussiness logic. 
	f)  tests.py

Create hello world application using django
--------------------------------------------------------
1. First we create the project.
2. Then we create the application name as myapp.
3. We registered our app into settings.py --> installed_apps
4. Then run the project using manage.py runserver.
