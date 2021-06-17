FROM python:3.9-slim

ENV HOME="/home/outflink"

WORKDIR ${HOME}

RUN mkdir ${HOME}/api

# List packages here
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    file        \
    gcc         \
    libwww-perl \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip


COPY requirements.txt ${HOME}/api
RUN pip install -r ${HOME}/api/requirements.txt

COPY app/ ${HOME}/api/app/
COPY migrations/ ${HOME}/api/migrations/
COPY alembic.ini ${HOME}/api
COPY *.sh ${HOME}/api/
RUN chmod +x ${HOME}/api/*.sh


EXPOSE 8000
