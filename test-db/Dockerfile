FROM ab1997/postgres:12-postgis-3

LABEL maintainer Camptocamp "info@camptocamp.com"

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB pyramid_oereb

COPY *.sql /docker-entrypoint-initdb.d/
