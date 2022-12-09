# Instalación de dependencias por comando de Django + django rest framework + psycopg (driver postgresql)

pip install django==4.0.1 djangorestframework psycopg2

# Instalación de dependencias desde un archivo (requeriments.txt)

pip install -r requeriments.txt

# Comando para crear listado de dependencias (librerias)

pip freeze > requeriments.txt

# Comando para generar models.

python manage.py inspectdb

python manage.py inspectdb > core/persistencia/models.py

# Comando para desplegar aplicación

python manage.py runserver 8000
