# Project Identity: Trevor's Developer Portfolio
**Goal:** Public resume and modular "project dump" for software engineering journey.

## 🛠 Tech Stack & Constraints
- **Backend:** Python 3.11+, Flask, SQLAlchemy.
- **Frontend:** Jinja2 Template Inheritance, HTML/CSS (Modular Asset Management).
- **Infrastructure:** uv (Package Manager), Gunicorn (Production WSGI), PostgreSQL.
- **Environment:** Windows (Dev) / Ubuntu-WSL (Testing) / DigitalOcean Droplet (Production).

## 🏛 Architecture: Martin's Clean Architecture
- **Layer 1 (Domain):** Entities and pure business logic (no dependencies).
- **Layer 2 (Service):** Use cases and request orchestration.
- **Layer 3 (Adapters):** Database repositories and interface translations.
- **Layer 4 (Infrastructure):** Flask routes, templates, and external tools.
- **The Rule:** Dependencies must always point **inward** toward the Domain.

## 📜 Development Rules for AI Agents
- **No Dense Paragraphs:** Use short, punchy bullet points and **bold keywords**.
- **Socratic Approach:** Prompt me with probing questions before generating solutions.
- **Zero-Guessing:** If context is missing, state "I don't know."
- **Deployment:** Always run `uv pip compile pyproject.toml -o requirements.txt` before pushing.
- **Clean Code:** Prioritize modularity and DRY principles. 

## 🚀 Simulation Strategy
- **Hybrid Approach:** Use Python/Flask for algorithm-heavy logic; use JS/Canvas for visual-heavy interactivity. 
- **Secrets:** Never hard-code credentials; use `.env` files via `python-dotenv`.