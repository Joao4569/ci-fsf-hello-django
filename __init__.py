"""
docstring
"""
import os


if os.environ.get("DEVELOPMENT") == "True":
    os.environ.get("DB_URL")
else:
    os.environ.get("DATABASE_URL")
