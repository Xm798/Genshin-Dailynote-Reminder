FROM python:3.7-alpine
ENV TZ=Asia/Shanghai

WORKDIR /tmp
COPY ./requirements.txt ./
RUN adduser app -D \
    && apk add --no-cache tzdata \
    && apk add --no-cache build-base \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-base\
    && rm -rf /tmp/*

WORKDIR /app
COPY index.py ./
COPY dailynotereminder ./dailynotereminder
RUN ln -sf dailynotereminder dailynoterhelper

USER app
CMD [ "python3", "./index.py" ]