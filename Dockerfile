FROM python:latest
RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /app/requirements1.txt
RUN pip install -r requirements1.txt
ADD . /app
CMD ["python", "app.py"]
EXPOSE 80
