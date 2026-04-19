FROM python:3.11

WORKDIR /app

COPY app.py .

RUN pip install flask gunicorn

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
