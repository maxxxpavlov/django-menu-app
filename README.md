# Древовидное меню
![Usecase](usecase.gif?raw=true "Пример")
## Запуск с помощью докера
```bash
docker-compose up --build db menu-app
```

## Запуск без докера
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata ./menu/seed/menutree.json
python manage.py createsuperuser
python manage.py runserver
```

Меню будет доступно по ссылке [127.0.0.1:8000](http://127.0.0.1:8000/)

Пароль и логин от админки admin:admin