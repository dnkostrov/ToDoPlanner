# ToDoPlanner

ToDoPlanner - учебный проект, приложение для хранения списка дел на неделю.
Данные хранятся в оперативной памяти и стираются при отключении сервиса.

## Структура проекта

ToDoPlanner/
├── ToDoPlanner.py          # Основной файл с кодом API
├── requirements.txt        # Зависимости для продакшена
├── requirements-dev.txt    # Зависимости для разработки и тестирования
├── test_ToDoPlanner.py     # Файл с тестами
├── .env.example            # Шаблон переменных окружения
├── .gitignore
└── README.md


### Установка и настройка

1. Клонируйте репозиторий:
	git clone https://github.com/dnkostrov/ToDoPlanner.git 
	cd ToDoPlanner

2. Создайте и активируйте виртуальное окружение:
	python3 -m venv venv
	source venv/bin/activate

3. Установите зависимости:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

4. Запустите приложение:
	python3 -m uvicorn ToDoPlanner:app --reload --host 127.0.0.1 --port 8000

5. Запустите тесты:
	python3 -m pytest -v

6. Документацию приложения после его запуска можно найти по адресу: 
	http://127.0.0.1:8000/docs

7. Приложение использует следующие переменные окружения:
	WEEK_NUMBER — номер текущей недели (по умолчанию: 1)
	PP_USER — имя пользователя приложения (по умолчанию: Пользователь)

8. Проверка эндпоинтов /health и /version выполняется через браузер или cURL:
	Health-check: curl http://127.0.0.1:8000/health (возвращает {"status": "ok"})
	Версия: curl http://127.0.0.1:8000/version (возвращает версию API и Python)

9. Логи приложения выводятся прямо в терминал, где запущен uvicorn, так как в коде настроен базовый обработчик logging.basicConfig(level=logging.INFO).

10. Для эксплуатации или обычного запуска, когда автоматическая перезагрузка не требуется, используйте команду без флага --reload:
	uvicorn ToDoPlanner:app --host 0.0.0.0 --port 8000
