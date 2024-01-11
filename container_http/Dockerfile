FROM python:3.8-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache nano procps && \
    rm -rf /var/cache/apk/*
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python", "app.py"]
CMD ["sleep", "infinity"]
