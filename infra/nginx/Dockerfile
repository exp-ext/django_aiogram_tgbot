FROM nginx:latest

# Установка переменных окружения из файла .env
ARG DOMAIN_NAME \
    DEBUG
ENV DOMAIN_NAME=${DOMAIN_NAME} \
    DEBUG=${DEBUG}

# Удаление файла конфигурации по умолчанию
RUN rm /etc/nginx/conf.d/default.conf

# Выбор нужного файла конфигурации на основе значения переменной DEBUG
COPY nginx$DEBUG.conf /etc/nginx/conf.d/nginx.conf

# Замена переменной в конфигурационном файле
RUN sed -i "s/DOMAIN_NAME/$DOMAIN_NAME/g" /etc/nginx/conf.d/nginx.conf
