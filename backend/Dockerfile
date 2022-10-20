FROM python:3
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

# https://forums.docker.com/t/docker-is-running-but-i-cannot-access-localhost-flask-application/82193/2
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV DEBUG_MODE=True
# CMD flask --app main.py run