####################################################################################################
## Builder image
####################################################################################################
FROM python:3.10-slim-bullseye AS builder

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt update \
    && apt install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /Reina

COPY /pyproject.toml /Reina/
COPY /poetry.lock /Reina/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip wheel --wheel-dir=/Reina/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.10-slim-bullseye

RUN apt update \
    && apt install -y --no-install-recommends \
    tini \
    ca-certificates \
    bash

WORKDIR /Reina

COPY /Bot/reina.py /Reina/Bot/
COPY /Bot/reinacore.py /Reina/Bot/
COPY /Bot/Cogs/ /Reina/Bot/Cogs
COPY /Bot/Libs/ /Reina/Bot/Libs
COPY /Scripts/postgres-seeder.py /Reina/postgres-seeder.py
COPY /Docker/Debian-Docker/start.sh /Reina/start.sh
COPY /Docker/Debian-Docker/wait-for /Reina/wait-for

COPY --from=builder /Reina/wheels /Reina/wheels
COPY --from=builder /Reina/requirements.txt /Reina/requirements.txt

RUN pip install --upgrade pip setuptools

RUN adduser --disabled-password --gecos "" reina \
    && chown -R reina:reina /Reina \
    && chmod +x /Reina/start.sh \
    && chmod +x /Reina/wait-for

USER reina

RUN pip install --user --no-index --find-links=/Reina/wheels -r requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["/Reina/start.sh"]

STOPSIGNAL SIGTERM

LABEL org.opencontainers.image.title="Reina"
LABEL org.opencontainers.image.description="A production-ready version of Beryl"
LABEL org.opencontainers.image.url="https://github.com/No767/Reina"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Reina"