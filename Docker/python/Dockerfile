FROM python:3.12

# Set work directory
WORKDIR /app

# Install dependencies
COPY /../../python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY /../../python .

