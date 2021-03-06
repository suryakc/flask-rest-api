FROM python:3.7.6-stretch

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src /app

#ENTRYPOINT [ "python" ]

#CMD [ "app.py" ]

CMD ["uwsgi","app.ini"]