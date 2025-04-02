# API для YAtuba
Учебный проект, ползы для окружающих не несет.

# Установка
Клонирование репозитория
```bash
git clone https://github.com/kanzenmuketsu/api_final_yatube

cd api_final_yatube/yatube_api
```
Выполнение миграций
```bash
python manage.py migrate
```
Запуск сервера
```bash
python manage.py runserver
```

# Основные end-поинты
* ***/api/v1/users/me***
* ***/api/v1/jwt/create/***
* ***/api/v1/jwt/refresh/***
* ***/api/v1/posts/***
* ***/api/v1/groups/***
* ***/api/v1/follow/***
* ***/api/v1/comments/***
* ***/redoc/***

# Примеры ответов

### /api/v1/posts/
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### /api/v1/groups/
```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```