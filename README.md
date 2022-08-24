<div align=center>

# Reina

![Reina](./Assets/reina-logo-resized.png)


[![Required Python Version](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://github.com/No767/Reina/blob/dev/pyproject.toml) [![CodeQL](https://github.com/No767/Reina/actions/workflows/codeql.yml/badge.svg?branch=dev&event=push)](https://github.com/No767/Reina/actions/workflows/codeql.yml) [![Snyk](https://github.com/No767/Reina/actions/workflows/snyk.yml/badge.svg?branch=dev&event=push)](https://github.com/No767/Reina/actions/workflows/snyk.yml) [![Docker Build (GHCR)](https://github.com/No767/Reina/actions/workflows/docker-build-ghcr.yml/badge.svg?branch=dev)](https://github.com/No767/Reina/actions/workflows/docker-build-ghcr.yml) [![Docker Build (Docker Hub)](https://github.com/No767/Reina/actions/workflows/docker-build-hub.yml/badge.svg)](https://github.com/No767/Reina/actions/workflows/docker-build-hub.yml)


A production-ready fork of Beryl

<div align=left>

## Info

Beryl is a small scale bot but for fun by one of my friends. I looked through the code, and found it extremely hard to figure out what is going on, and even to how to use Beryl. Reina solves that issue. Slash command integration, documented features, and a near complete rewrite of the whole entire bot. The events system was originally loading them from a literal JSON file. This can cause major issues, and thus i spent some time rewriting Beryl by swapping that out with a SQL based events system, and many more things. The purpose of Reina is to see how the new changes would actually deploy and work in production

## Features

Currently implemented:

- Custom XP system (DisQuest)
- Events system
- AniList, MAL, MangaDex, Jisho, and Tenor Support
- Kumiko's Genshin Wish Sim 
- Rewritten features of Beryl

Considering implementing:

- Kumiko's Economy System

## Invite

This is meant to be a private bot, so no public listings or invites of Reina will be made

## Licensing

Parts of Reina come directly from Beryl, and thus credit needs to be given to such places. Any modifications that Reina makes to Beryl are licensed under Apache-2.0.
