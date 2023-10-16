## Django приложение реализовывающее древовидное меню категорий

### Установка приложения

#### Загрузите репозиторий с помощью команды:
`git clone https://github.com/kenunq/tree_menu.git`

#### Создайте виртуальное окружение:
`python -m venv venv`

#### Установите зависимости необходимые для работы приложения:
`pip install -r requirements.txt`

#### Единоразово выполните команды создания базы данных:
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py loaddata main\fixtures\data_dump.json`

#### Для запуска программы выполните команду:
`python manage.py runserver`

#### Откройте в браузере приложение по адресу:
`http://127.0.0.1:8000`

#### Для остановки программы нажмите сочетание клавиш CTRL+C
