# 🚀 FastAPI Backend Boilerplate

This is a backend boilerplate built with **FastAPI** and **Poetry**, designed with scalability, modularity, and developer productivity in mind. It supports multiple folder structures, integrates powerful tooling like **Semantic Release** for versioning, and follows clean architectural patterns.

## 🧰 Tech Stack

- **FastAPI** – Modern, fast web framework for APIs
- **Poetry** – Python dependency management and packaging
- **PostgreSQL** – Powerful, open-source relational database
- **Alembic** – Lightweight database migrations using SQLAlchemy
- **Semantic Release** – Automated changelog generation, versioning, and releases

## 📁 Folder Structure

This project supports two folder structures based on developer preference or project size:

### 1. Global Modular Structure

Suitable for small to mid-sized projects:

```
app/
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas
├── crud/           # CRUD operations
├── services/       # Business logic
├── utils/          # Utility functions
├── constants/      # Global constants and enums
├── providers/      # Dependency injection providers
├── main.py         # Entry point for the FastAPI app
```

### 2. Feature-Based (Domain-Driven) Structure

Recommended for larger applications or domain-heavy systems:

```
app/
├── user/
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── exceptions.py
│   └── routes.py
├── product/
│   ├── ...
├── common/
│   ├── utils/
│   ├── services/
│   ├── constants/
│   └── providers/
├── main.py
```

> ✅ You can choose the structure that suits your project. Both are supported by the core logic.

---

## 🧪 Testing

You can use [pytest](https://docs.pytest.org/) for writing and running unit tests:

```bash
pytest
```

Example test structure:

```
tests/
├── test_user/
│   ├── test_crud.py
│   └── test_routes.py
├── test_utils/
```

---

## 📦 Semantic Release

This project uses **Semantic Release** for:

- Automating version numbers (following semver)
- Auto-generating changelogs
- Creating Git tags

### Commit Examples (Conventional Commits)

- `feat: add user registration endpoint`
- `fix: correct token expiration bug`
- `refactor: clean up auth service logic`
- `chore: update dependencies`

---

## 🛠️ Database Migrations

Using **Alembic** with SQLAlchemy models:

Create a migration:

```bash
alembic revision --autogenerate -m "Add user table"
```

Apply migrations:

```bash
alembic upgrade head
```

Database settings are configured in `alembic.ini` and typically in a `settings.py` file using environment variables.

---

## ⚙️ Getting Started

1. **Clone the repo**

```bash
git clone https://your-repo-url.git
cd your-project
```

2. **Install dependencies**

```bash
poetry install
```

3. **Run the app**

```bash
poetry run uvicorn app.main:app --reload
```

4. **Run database migrations**

```bash
alembic upgrade head
```

---

## 🧩 Additional Components

- `utils/` – Common utility/helper functions
- `services/` – Business logic outside the CRUD layer
- `constants/` – Shared enums or constant values
- `providers/` – Dependency injection components or factory logic

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Taha Omar**

<!-- [your-website.com](https://your-website.com)   -->

Feel free to reach out for feedback or collaboration!

---
