FROM python:3.9-slim
WORKDIR /app
EXPOSE $PORT
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PORT=$PORT
EXPOSE $PORT
CMD ["gunicorn", "wsgi:app", "--log-file","-""--bind","0.0.0.0:$PORT"]
