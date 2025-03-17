<h1 align="center"> 📜 Change Log </h1>

<h3 align="center"> [0.1.0-beta] - 2025-03-12 </h3>

### 🆕 Added
- Initial API implementation using **FastAPI** and **GraphQL**.
- Setup **PostgreSQL** database integration.
- Implemented **JWT authentication** for secure user login.
- **Dockerized** the application for containerized deployment.
- Added **README** and **CHANGELOG** documentation.
- Initialized **Alembic** db migrations, including docker-compose auto migrations for changes on future ups.
### 🔄 Changed
- Optimized API response times by improving database query efficiency.
- Refactored folder structure for better project organization.
- Updated `docker-compose.yml` for streamlined development.

### 🐞 Fixed
- Resolved bug where `alembic` migrations were not detecting models correctly.
- Fixed issue with JWT expiration handling.
- Fixed incorrect import paths in `alembic/env.py`.

### 🗑️ Removed
- Removed unnecessary dependencies from `requirements.txt` to reduce build size.
- Removed old unused database tables.

---
