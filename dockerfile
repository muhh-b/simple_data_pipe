# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

# Run app.py when the container launches
CMD ["python", "flask_app/flask_app.py"]


# docker build -t monapp .
# docker run -p 5000:5000 monapp