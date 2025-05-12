FROM python:3.8-slim-buster

# COPY ./requirements.txt /app/requirements.txt
# RUN pip install -r requirements.txt
RUN pip3 install flask
WORKDIR /app

# COPY requirements.txt requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]