From python:3.9-alpine

RUN apk update && apk add expect \
    && apk add postgresql-dev gcc python3-dev musl-dev            
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /visaAlliance2phase

WORKDIR /visaAlliance2phase

COPY . .
RUN chmod +x ./docker-entrypoint.sh
RUN pip install -r requirements.txt --no-cache-dir
RUN apk del .tmp
ENTRYPOINT ["sh","./docker-entrypoint.sh"]
EXPOSE 8080
