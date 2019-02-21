Пример того как можно использовать `dramatiq-tasks-manager <https://github.com/cthtuf/dramatiq-tasks-manager>`_:

1. Установить pip install dramatiq-tasks-manager
2. Добавить необходимые настройки для apscheduler, dramatiq, dramatiq_tasks_manager
3. Создать приложение, содержащее файл tasks со списком задач (Actors) dramatiq.

Profit!

Для запуска необходимо иметь доступный сервер postgresql, redis, rabbit.
Чтобы запустить приложение, необходимо запустить dramatiq-воркер, а так же запустить api
В самом простом виде это выглядит так::

    python manage.py rundramatiq
    python manage.py runserver

Для получения списка выполненных задач::

    curl -X GET http://localhost:8000/tasks/executed

Для получения деталей выполненной задачи::

    curl -X GET http://localhost:8000/tasks/executed/:task_id

Для запуска задачи на выполнение::

    curl -X POST http://localhost:8000/tasks/execute -d '{"actor_name": "taskname", kwargs={"task_param1": "param_value1"}'

Для отправки задачи в планировщик::

    curl -X POST http://localhost:8000/tasks/schedule -d '{"func": "print_result", "trigger": "date", "run_date": "2019-02-11T07:31:00Z", "kwargs": {"message_data": {"message_id": "```"}, "result": "OK"}}'
