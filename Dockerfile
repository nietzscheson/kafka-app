FROM python:3.8

RUN pip3 install --upgrade pip

RUN pip3 install awscli --upgrade --user --no-warn-script-locatio

COPY requirements.txt .

RUN pip install -r requirements.txt

