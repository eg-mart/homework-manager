FROM python:3-alpine
wORKDIR /app
COPY . .
RUN echo "Installing dependencies..."
RUN python -m pip install -r requirements.txt
RUN echo "Starting web app..."
EXPOSE 5000
CMD python main.py ; python bot/main.py
