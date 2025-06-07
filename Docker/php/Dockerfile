FROM php:8.4-fpm

FROM php:8.4-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    bash \
    git \
    unzip \
    libzip-dev \
    libicu-dev \
    zlib1g-dev \
    libonig-dev \
    curl

# Install PHP extensions
RUN docker-php-ext-install \
    intl \
    pdo \
    pdo_mysql \
    opcache \
    zip

# Install Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Set working directory
WORKDIR /var/www/html

# Copy application files
COPY ../../php .

# Set permissions
RUN chown -R www-data:www-data /var/www/html

# Expose port 9000 and start php-fpm server
EXPOSE 9000
CMD ["php-fpm"]
