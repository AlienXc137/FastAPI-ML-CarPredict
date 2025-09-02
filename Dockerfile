FROM python:3.10

WORKDIR /app

COPY . .
# copying all of working directory to /app (docker) in container

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]