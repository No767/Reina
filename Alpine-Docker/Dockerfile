####################################################################################################
## Builder image
####################################################################################################
# Credits to Ellie (@TheSilkky) for the original system + Dockerfile
# Modifed for use with Poetry
FROM python:3.10.6-alpine3.16 AS builder

RUN apk add --no-cache \
    ca-certificates \
    build-base \
    curl \
    linux-headers

# Add Poetry locally
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /Reina

COPY /pyproject.toml /Reina/
COPY /poetry.lock /Reina/


# Create dependency wheels
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip wheel --wheel-dir=/Reina/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.10.6-alpine3.16

RUN apk add --no-cache \
    ca-certificates \
    tini \
    bash

WORKDIR /Reina

COPY /Bot/reina.py /Reina/Bot/
COPY /Bot/Cogs/ /Reina/Bot/Cogs
COPY /Bot/genshin_wish_sim_utils/ /Reina/Bot/genshin_wish_sim_utils
COPY /Bot/help_utils/ /Reina/Bot/help_utils

# Copy dependency wheels from builder stage
COPY --from=builder /Reina/wheels /Reina/wheels
COPY --from=builder /Reina/requirements.txt /Reina/requirements.txt

COPY /Alpine-Docker/start.sh /Reina/start.sh

RUN pip install --upgrade pip setuptools wheel

# Add an unprivileged user and set directory permissions
RUN adduser --disabled-password --gecos "" reina \
    && chown -R reina:reina /Reina \
    && chmod +x /Reina/start.sh

USER reina

# Install dependencies
RUN pip install --user --no-index --find-links=/Reina/wheels -r requirements.txt

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["/Reina/start.sh"]

STOPSIGNAL SIGTERM

# Image metadata
LABEL org.opencontainers.image.title="Reina"
LABEL org.opencontainers.image.description="A production-ready version of Beryl"
LABEL org.opencontainers.image.url="https://github.com/No767/Reina"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Reina"