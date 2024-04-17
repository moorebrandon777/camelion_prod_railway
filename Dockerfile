# Use Python as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV CHROMEDRIVER_VERSION 123.0.6312.122 
ENV CHROMEDRIVER_PATH /usr/local/bin/chromedriver

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev \
        gcc \
        wget \
        unzip \
        gnupg \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set up Chrome repository and install Chrome
RUN wget -q -O /tmp/key.pub https://dl.google.com/linux/linux_signing_key.pub \
    && apt-key add /tmp/key.pub \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Download and install ChromeDriver
RUN wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/123.0.6312.122/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container at /code
COPY . /code/

# Install Gunicorn
RUN pip install gunicorn

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "camelion.wsgi:application"]
