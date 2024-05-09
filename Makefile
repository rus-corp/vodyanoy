run:
	python manage.py runserver

mm:
	python manage.py makemigrations

mi:
	python manage.py migrate

apps:
	python manage.py startapp "$(c)"

drop:
	dropdb -U postgres vodyanoy

create:
	createdb -U postgres vodyanoy

superuser:
	python manage.py createsuperuser