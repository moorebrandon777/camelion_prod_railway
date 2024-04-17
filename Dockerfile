# Use Python as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV CHROMEDRIVER_PATH /usr/local/bin/chromedriver

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev \
        gcc \
        wget \
        unzip \
        libgconf-2-4 \
        libnss3 \
        libxi6 \
        libgconf-2-4 \
        libxtst6 \
        libxss1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt /code/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Download and install ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Copy the project code into the container at /code
COPY . /code/

# Install Gunicorn
RUN pip install gunicorn

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]
