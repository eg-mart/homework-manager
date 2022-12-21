FROM python:3-alpine
wORKDIR /app
COPY . .
RUN chmod +x /app/start.sh
RUN echo "Installing dependencies..."
RUN python -m pip install -r requirements.txt
RUN echo "Starting web app..."
EXPOSE 5000
CMD /app/start.sh
