FROM python:3.12.2-alpine

RUN mkdir application

WORKDIR /application

COPY requirements.txt .

RUN pip install - r requirements.txt

RUN mkdir web_server

WORKDIR /web_server

COPY /web_server .

CMD [ "uvicorn", "main:web_server", "--reload"]