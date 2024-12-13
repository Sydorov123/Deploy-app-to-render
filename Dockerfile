# Використовуємо офіційний образ Python
FROM python:3.9-slim

# Встановлення робочої директорії
WORKDIR /app

# Копіюємо файли в контейнер
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду
COPY . .

# Запуск додатку
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
