FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

RUN mkdir application

WORKDIR /application

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir web_server

WORKDIR /web_server

COPY ./web_server .

CMD [ "uvicorn", "main:web_server", "--host", "0.0.0.0", "--port", "8000"]