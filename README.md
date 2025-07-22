# Lawyer Site

Юридический сайт на Django с формой обратной связи, интеграцией с Google Таблицей через Google Форму и современным дизайном.

## Быстрый старт локально

1. Клонируйте репозиторий:
   ```bash
   git clone <ваш-репозиторий>
   cd <ваша-папка>
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Примените миграции:
   ```bash
   python manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. Откройте http://127.0.0.1:8000

## Деплой на Render.com

1. Загрузите проект на GitHub.
2. На https://render.com создайте новый Web Service:
   - Укажите репозиторий.
   - Build Command: `pip install -r requirements.txt && python manage.py migrate`
   - Start Command: `gunicorn lawyer_site.wsgi:application`
   - Python Version: 3.10+
3. В настройках Render добавьте переменные окружения:
   - `DJANGO_SECRET_KEY` — ваш секретный ключ (или используйте из settings.py)
   - `DJANGO_DEBUG` — `False`
   - `ALLOWED_HOSTS` — `*` или ваш домен
4. Для статики:
   - В Render настройте Static Site для папки `staticfiles/` (если нужно).
   - Или используйте WhiteNoise (добавьте в MIDDLEWARE и настройте STATIC_ROOT).

## Важно
- Для работы формы с Google Таблицей ничего дополнительно на сервере настраивать не нужно — интеграция идёт через Google Form.
- Для почты используется console backend (можно изменить в settings.py).

---

**Вопросы:** пишите в Issues или на почту Allazov009@mail.ru 