"""
docstring
"""
import os
import re


if os.environ.get("DEVELOPMENT") == "True":
    os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    # app.config["..."] = uri # heroku
