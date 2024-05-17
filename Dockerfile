FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY run.py /app

ENV FLASK_RUN_PORT=5000
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["python", "run.py"]
