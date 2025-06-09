FROM python:3.12

# Set work directory
WORKDIR /app

# Install dependencies
COPY /../../python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

RUN playwright install-deps

# Copy your code
COPY /../../python .

