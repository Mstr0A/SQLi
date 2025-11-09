# SQL Injection Demo

A simple Flask application demonstrating SQL injection vulnerabilities for
educational purposes.

## ⚠️ WARNING

This application is **intentionally vulnerable** and should **NEVER** be used in
production. It is designed solely for educational purposes to demonstrate how
SQL injection attacks work.

## Setup

1. Clone the repository

```bash
git clone https://github.com/Mstr0A/SQLi
cd SQLi
```

2. Install dependencies

```bash
pip install flask mysql-connector-python

# [OPTIONAL] use uv if you have it

uv sync
```

3. Configure database connection

- The database schema can be found in `database.sql`
- Copy `db_example.py` to `db.py`
- Update the database credentials in `db.py`

```bash
cp db_example.py db.py
```

4. Run the application

```bash
python main.py
```

5. Open your browser and navigate to `http://127.0.0.1:5000`

## SQL Injection Examples

Try these in the username field:

- `' OR '1'='1' --` (bypass login)
- `admin' --` (comment out password check)
- `' OR 1=1 #` (alternative comment syntax)

## Project Structure

```
.
├── main.py              # Flask application
├── db.py               # Database connection (not in repo)
├── db_example.py       # Example database config
└── templates/
    ├── index.html      # Login page
    └── result.html     # Result page
```

## Educational Use Only

This project demonstrates why you should **always use parameterized queries** or
prepared statements in production code.

**Never do this:**

```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```

**Always do this:**

```python
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```
