[README.md](https://github.com/user-attachments/files/34890376/README.md)
# Лендинг-сайт на Django: Магазин чая

Данный проект представляет собой лендинг-сайт, разработанный в рамках лабораторной работы по изучению фреймворка Django.

## Описание темы
Сайт был создан для ознакомления с Django, в виде интернет магазина. Тут вы найдете различные виды и цены чаев на любой выбор.

## Реализованные функции
В ходе выполнения лабораторной работы были реализованы следующие требования:
- Создан Django-проект и приложение `landing`.
- Создана модель `Item` с более чем 5 полями.
- Настроен Django Admin для управления контентом.
- Реализована маршрутизация (главная страница, детальная страница товара/услуги, страница контактов).
- Настроено наследование шаблонов через `base.html`.
- Вывод данных из базы данных с помощью цикла `{% for %}`.
- Подключены статические файлы (CSS) и медиафайлы (изображения).
- **(Бонус)** Реализована форма обратной связи (с защитой CSRF).
- **(Бонус)** Использованы слаги в URL (`SlugField`).

## Инструкция по запуску проекта

Для того чтобы запустить проект на локальном компьютере, выполните следующие шаги:
# 1. Клонировать репозиторий
git clone <url>
cd <LandingProject>

# 2. Создать виртуальное окружение
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\Activate.ps1       # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py migrate

# 5. Создать суперпользователя
python manage.py createsuperuser

# 6. Запустить сервер
python manage.py runserver

### Скриншоты кода
![Settings.py](screenshots/4.png)
![Settings.py](screenshots/1.png)
![Settings.py](screenshots/2.png)
![Settings.py](screenshots/5.png)
![Settings.py](screenshots/3.png)

### Скриншоты сайта
![Settings.py](screenshots/glavnaya.png)
![Settings.py](screenshots/admin-sait.png)
![Settings.py](screenshots/detail-site.png)
![Settings.py](screenshots/wishlist-sait.png)	


