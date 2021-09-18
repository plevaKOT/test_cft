FROM python:3.8
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir -p /var/www/app/

WORKDIR /var/www/app/

COPY . /var/www/app/

RUN cd /var/www/app/

RUN pip install -r requirements.txt

ENV FLASK_APP app.py

ENTRYPOINT ["python"]

CMD ["app.py"]
