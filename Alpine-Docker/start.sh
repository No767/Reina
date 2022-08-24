#!/usr/bin/env bash

# Bot Token
if [[ -v REINA_TOKEN ]]; then
    echo "Reina_Token=${REINA_TOKEN}" >> /Reina/Bot/.env
else
    echo "Missing bot token! REINA_TOKEN environment variable is not set."
    exit 1;
fi

# Hypixel API Keys
if [[ -v HYPIXEL_API_KEY ]]; then
    echo "Hypixel_API_Key=${HYPIXEL_API_KEY}" >> /Reina/Bot/.env
else
    echo "Missing Hypixel API key! HYPIXEL_API_KEY environment variable is not set."
fi 

if [[ -v TENOR_API_KEY ]]; then
    echo "Tenor_API_Key=${TENOR_API_KEY}" >> /Reina/Bot/.env
else
    echo "Missing Tenor API key! TENOR_API_KEY environment variable is not set."
fi 


if [[ -v POSTGRES_PASSWORD ]]; then
    echo "Postgres_Password=${POSTGRES_PASSWORD}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_Password env var! Postgres_Password environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_IP ]]; then
    echo "Postgres_IP=${POSTGRES_IP}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_IP env var! POSTGRES_IP environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_USER ]]; then
    echo "Postgres_User=${POSTGRES_USER}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_User env var! POSTGRES_USER environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_DISQUEST_DATABASE ]]; then
    echo "Postgres_Database=${POSTGRES_DISQUEST_DATABASE}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_Disquest_Database env var! POSTGRES_DISQUEST_DATABASE environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_EVENTS_DATABASE ]]; then
    echo "Postgres_Events_Database=${POSTGRES_EVENTS_DATABASE}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_Events_Database env var! POSTGRES_EVENTS_DATABASE environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_WS_DATABASE ]]; then
    echo "Postgres_Wish_Sim_Database=${POSTGRES_WS_DATABASE}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_Wish_Sim_Database env var! POSTGRES_WS_DATABASE environment variable is not set."
    exit 1;
fi

if [[ -v POSTGRES_PORT ]]; then
    echo "Postgres_Port=${POSTGRES_PORT}" >> /Reina/Bot/.env
else
    echo "Missing Postgres_Port env var ! POSTGRES_PORT environment variable is not set."
    exit 1;
fi

exec python3 /Reina/Bot/reina.py