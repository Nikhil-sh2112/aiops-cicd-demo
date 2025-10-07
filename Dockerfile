FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY aiops_web.py .

COPY system_logs.txt .

EXPOSE 80 

CMD ["python", "aiops_web.py"]
