set -e
python manage.py migrate
python manage.py loaddata ./menu/seed/menutree.json
python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:8000 --noreload