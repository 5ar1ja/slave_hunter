# Slave Hunter 🕵️‍♂️

Django REST API для управления компаниями, пользователями и авторизацией.

## 📦 Технологии

- Python 3.11+
- Django 4+
- Django REST Framework
- PostgreSQL (или SQLite для локального запуска)
- dotenv (.env конфигурация)

---

## 🚀 Быстрый старт

### 1. Клонирование проекта

```bash
git clone https://github.com/yourusername/slave_hunter.git
cd slave_hunter

Создани и активация виртуальной среды
python -m venv venv
source venv/bin/activate           # Для Linux/macOS
venv\Scripts\activate              # Для Windows

pip install -r requirements.txt

cp .env.example .env

генерация ключа
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
