# Use Python as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
# ENV CHROMEDRIVER_VERSION 94.0.4606.61
ENV CHROMEDRIVER_PATH /usr/local/bin/chromedriver
ENV PORT 8000

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-dev \
        gcc \
        wget \
        curl \
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
# RUN wget -q -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.60/linux64/chromedriver-linux64.zip \
#     && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
#     && rm /tmp/chromedriver.zip \
#     && chmod +x /usr/local/bin/chromedriver

RUN CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.60/linux64/chromedriver-linux64.zip" \
    && echo "Downloading ChromeDriver from $CHROMEDRIVER_URL" \
    && wget -q -O /tmp/chromedriver.zip $CHROMEDRIVER_URL \
    && echo "Extracting ChromeDriver zip file" \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && echo "Cleaning up" \
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

# Copy entry script into the container at /code
COPY entry.sh /code/

# Make the entry script executable
RUN chmod +x /code/entry.sh

# Install Gunicorn
RUN pip install gunicorn

# Expose port 8000 to the outside world
EXPOSE $PORT

# Set the entry point
ENTRYPOINT ["/code/entry.sh"]

# Command to run the Django application using Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "your_project.wsgi:application"]
