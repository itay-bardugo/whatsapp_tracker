FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH /app

ENTRYPOINT ["python", "whatsapp_tracker/wt_main.py"]
