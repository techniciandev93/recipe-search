# Бот по поиску рецептов блюд

## Как установить

Python 3.8 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Создайте файл `.env` в корневой директории проекта и добавьте переменную окружения:

```
TELEGRAM_BOT_API_TOKEN=Ваш токен для бота
SECRET_KEY=Ваш секретный ключ для django
DEBUG_DJANGO=true или ничего для false
```
## Как запустить
Для запуска бота
```
python manage.py bot
```
Для создания таблиц проведите миграции
```
python manage.py makemigrations
python manage.py migrate
```
Для запуска веб сервера
```
python manage.py runserver
```
Для входа в админку создайте учётную запись
```
python manage.py createsuperuser
```
И авторизуйтесь http://127.0.0.1:8000/admin/