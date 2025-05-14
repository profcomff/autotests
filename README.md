# Автотесты

Этот репозиторий служит фундаментом для написания автотестов с использованием Playwright и Pytest, с возможностью интеграции с Kiwi TCMS.

## Структура проекта

-   `requirements.txt`: Список зависимостей проекта.
-   `settings.py`: Глобальные настройки проекта с использованием Pydantic.
-   `tests/`: Директория для всех тестов.
    -   `tests/conftest.py`: Файл для общих фикстур Pytest.
    -   `tests/test_example.py`: Пример базового теста с Playwright и фикстурой.
    -   `tests/rating/`: Директория для тестов API рейтинга.
        -   `tests/rating/test_lecturer.py`: Тесты для эндпоинтов преподавателей API рейтинга.
-   `kiwi_integration/`: Директория для интеграции с Kiwi TCMS.
    -   `kiwi_integration/kiwi_client.py`: Базовый клиент для взаимодействия с Kiwi TCMS API.

## Установка зависимостей

Рекомендуется использовать [виртуальное окружение](https://docs.python.org/3/library/venv.html) для управления зависимостями проекта.

1.  **Создайте виртуальное окружение** (если оно еще не создано) в корневой директории проекта:

    ```bash
    python -m venv venv
    ```

2.  **Активируйте виртуальное окружение**:

    *   На macOS и Linux:

        ```bash
        source venv/bin/activate
        ```

    *   На Windows (Command Prompt):

        ```bash
        venv\Scripts\activate.bat
        ```

    *   На Windows (PowerShell):

        ```bash
        venv\Scripts\Activate.ps1
        ```

3.  **Установите зависимости** из `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

После установки зависимостей Playwright также требует установки необходимых браузерных бинарников. Выполните:

```bash
playwright install
```

## Запуск тестов

Для запуска всех тестов в проекте, находясь в корневой директории, выполните:

```bash
pytest
```
