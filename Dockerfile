FROM python:alpine3.18

ENV DEBUG=True
ENV SECRET_KEY=django-insecure-=(8*a1#nry)h4o=d!i#ch3$vi%e@k=2564x3a^ad!2e_j45l6n
ENV DB_ENGINE=django.db.backends.sqlite3
ENV DB_NAME=db.sqlite3

RUN addgroup app && adduser -S -G app app
USER app

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
