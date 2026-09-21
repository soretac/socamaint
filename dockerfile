FROM python:3.14.7-alpine3.24

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

WORKDIR /socamaint

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt





COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]