FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /srv

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "run.py"]