Deploy app to render

```markdown
# Flask API Deployment to Render

Цей проект є Flask API, який розгортається на платформі **Render**. API працює з базою даних PostgreSQL, яка налаштована через середовище змінних.

## Структура проекту

Проект має таку структуру:

```
my-flask-api/
│
├── app.py           # Основний код для Flask API
├── requirements.txt # Список залежностей Python
├── Dockerfile       # Файл для створення Docker-образу
├── render.yaml      # Налаштування для деплою на Render
├── Procfile         # Файл для запуску додатку на Render
└── .env             # Локальні змінні середовища (для налаштувань бази даних)
```

## Технології

- **Flask**: Мікрофреймворк для створення веб-додатків на Python.
- **SQLAlchemy**: ORM для роботи з базами даних.
- **PostgreSQL**: Система управління реляційними базами даних.
- **Render**: Платформа для хостингу веб-додатків та API.

## Налаштування

1. **Клонуйте репозиторій**:

   ```bash
   git clone https://github.com/yourusername/my-flask-api.git
   cd my-flask-api
   ```

2. **Налаштуйте змінні середовища**:

   Створіть файл `.env` у кореневій директорії та додайте такі змінні:

   ```
   DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database>
   ```

3. **Встановіть залежності**:

   Якщо ви хочете запустити додаток локально, створіть віртуальне середовище та встановіть залежності:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   pip install -r requirements.txt
   ```

4. **Запуск додатку локально**:

   Для локального запуску:

   ```bash
   python app.py
   ```

   Додаток буде доступний за адресою: `http://127.0.0.1:8080`.

## Деплой на Render

1. **Створіть репозиторій на Render**:

   Перейдіть на [Render](https://render.com) і створіть новий **Web Service**.

2. **Налаштуйте Render**:

   - Підключіть свій репозиторій до Render.
   - Вказуйте команду для збірки (`pip install -r requirements.txt`) та запуску (`gunicorn app:app --bind 0.0.0.0:8080`).
   - У файлі `render.yaml` вказується URL для підключення до вашої бази даних через змінну середовища `DATABASE_URL`.

3. **Запуск на Render**:

   Після налаштування ви можете деплоїти ваш додаток на Render, і він буде доступний через URL, наприклад:

   ```
   https://your-app-name.onrender.com
   ```

## Тестування API

Для тестування API після деплою на Render використовуйте cURL-запит:

```bash
curl 'https://your-app-name.onrender.com/api/v1/products' \
  -X 'GET' \
  -H 'Content-Type: application/json'
```

