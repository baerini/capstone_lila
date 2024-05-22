# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

COPY . .

# RUN apt-get update
# RUN apt-get install -y gcc
# RUN apt-get install -y libmysqlclient-dev
# RUN apt-get install -y pkg-config
# RUN rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Specify the entry point for the container to run the Flask app
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["python3", "main.py"]