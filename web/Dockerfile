FROM python:3.7-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY listen.py .
EXPOSE 8000
ENTRYPOINT ["/app/listen.py"]


# Docker build -t websocket .
# docker run --rm -p 8000:8000 websocket
# open websocket.html
