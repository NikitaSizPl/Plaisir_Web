# Используем официальный образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Указываем, что приложение будет слушать на порту 8000
EXPOSE 8000

# Запускаем приложение с использованием uvicorn
CMD ["uvicorn", "sql_app/main:app", "--host", "0.0.0.0", "--port", "8000"]