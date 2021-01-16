Веб-приложение для фастфуд-бизнеса.

На главном экране пользователь создает заказ, потом попадает на экран с составом своего заказа. Здесь все происходит
на уровне pyramid.

Заказы и бургеры, приписанные к заказу, записываются в базу данных SQLite. Чтобы посмотреть базу данных:
1. /list - для списка заказов, по ссылке переходим на бургеры, а еще можем поставить отметку выполнения
2. /burgers - список бургеров

Устройство проекта:
alembic - для миграций БД
classes - сущности заказа, бургера и т.д., их обработка
infrastructure - операции по обработке и перекидыванию данных
models - модели для sqlalchemy
scripts - для инициализации
static - стили, картинки
temlates - разметки jinja
views - обработчики рутов

Прикрепляем уже заполненнную тестовую БД для удобства.

pyramid_based_ber
=================

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd pyramid_based_ber

- Create a Python virtual environment, if not already created.

    python3 -m venv env

- Upgrade packaging tools, if necessary.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Load default data into the database using a script.

    env/bin/initialize_pyramid_based_ber_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
