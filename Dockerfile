FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python" ,"manage.py", "runserver", "--noreload","0.0.0.0:8000"]