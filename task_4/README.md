## Последний коммит был уже сделан после сдачи, так как узнал как правильно работать с сессиями в алхимии и нашел неправильное название функции и неправильный образ postgres, с прошлого проекта использовал postgis 

# Стэк
- Python(FastAPI)
- DB (Postgresql + SQLAlchemy)
- Docker + docker-compose
- pytest

# Запуск
```bash
cd task_4
docker-compose up
```
Открыть: http://127.0.0.1:8000/docs#/
Админка-бд: http://127.0.0.1:8090/
# Тесты
Замокал LinkService в файле mock.py.
Запустить тесты:
```bash
docker exec -it task_4-link-service-1 sh
pytest
```