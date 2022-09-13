# ✨ Reina v2.4.0 ✨

Fixes some bugs in regards with globally rolling out slash commands, and update any dependencies that needed to be updated. Also includes Debian-based builds
## 🛠️ Changes

- Globally roll out all slash commands instead (fixes 403 missing perms errors)
- Use Python 3.10.7 for all Dockerfiles
- Update Docker Compose example
- Use `github.actor` instead of `github.repository_owner` for Docker Build GHCR workflows
- Include Docker ENV examples
- Condense Docker Build workflows
- Don't make Alpine builds the latest for prod deployments

## ✨ Additions

- Debian-Based Dockerfiles

## ➖ Removals

## ⬆️ Dependency Updates

- \[pip](deps)\: Bump orjson from 3.7.12 to 3.8.0 (@dependabot)
- \[pip](deps)\: Bump python-dotenv from 0.20.0 to 0.21.0 (@dependabot)
- \[pip](deps)\: Bump py-cord from 2.1.1 to 2.1.3 (@dependabot)
- \[pip](deps)\: Bump numpy from 1.23.2 to 1.23.3 (@dependabot)
- \[pip](deps)\: Bump pysimdjson from 5.0.1 to 5.0.2 (@dependabot)