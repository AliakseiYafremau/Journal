# Журнал оценок 
## О проекте
Проект предназначен для создания и отслеживания оценок
Есть возможность
- Создавать предметы
- Выставлять процентное отношение оценок на среднее значени
- Добавлять и удалять оценки
- Регистрироваться и авторизироваться
## Запуск
Клонируйте репозиторий и перейдите в корневую папку
```bash
git clone https://github.com/AliakseiYafremau/Journal
cd Journal
```
Создайте виртуальное окружение
```bash
python -m venv venv
```
Активируйте виртуальное окружение
1. Активация на Windows
```
venv/Scripts/activate
```
2. Активация на Linux
```
source venv/bin/activate
```
Скачайте все библиотеки и загрузите миграции
```
pip install -r requirements.txt
python Diary/manage.py migrate
```
Запустите проект
```
python Diary/manage.py runserver
```