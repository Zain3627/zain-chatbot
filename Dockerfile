FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY raw-files/ raw-files/
COPY media/ media/
COPY main.py .

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]