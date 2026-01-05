FROM python:3.9-slim

WORKDIR /app

# Instala o catt e o flask
RUN pip install catt flask flask-basicauth yt-dlp

COPY . .

CMD ["python", "app.py"]
