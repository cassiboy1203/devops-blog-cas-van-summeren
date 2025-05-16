FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY custom_controller.py .

CMD kopf run custom_controller.py
