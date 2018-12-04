FROM ubuntu
RUN apt update
RUN apt -y install python3-pip
RUN pip3 install flask flask_cors
COPY . /app/
CMD ["python3", "/app/app.py"]
