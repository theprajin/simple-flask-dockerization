FROM python:3.10

WORKDIR /first_flask_app

RUN groupadd -g 1000 systemadmin && useradd -m -u 1000 -g 1000 -s /bin/bash -d /first_flask_app systemadmin

COPY ./requirements.txt /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
COPY ./wait-for-psql.py /usr/local/bin/wait-for-psql.py

RUN chmod +x /usr/local/bin/wait-for-psql.py /entrypoint.sh 

RUN pip install --upgrade pip && pip install -r /requirements.txt

# copy everyting from this dir to /app inside image/container
COPY . .

USER systemadmin
WORKDIR /first_flask_app
VOLUME ["/first_flask_app"]

# what command to run when container starts
# CMD ["python", "app.py"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["app"]
