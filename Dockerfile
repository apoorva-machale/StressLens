FROM python:3.12
# FROM redis:latest as redis
# FROM google/cloud-sdk:latest as google-cloud-sdk
WORKDIR /blog

# Copy the current directory contents into the container at /app
COPY . /blog

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 3000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "3000"]