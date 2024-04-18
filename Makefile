run:
	python manage.py runserver

mm:
	python manage.py makemigrations

mi:
	python manage.py migrate

apps:
	python manage.py startapp "$(c)"