import os

# Define directory structure
folders = [
    "app",
    "static",
    "templates",
    "model"
]

# Define files to create and their content
files = {
    "app/__init__.py": "",
    "app/routes.py": "# Flask routes will go here\n",
    "app/utils.py": "# Utility functions will go here\n",
    "static/style.css": "/* Add your custom styles here */\n",
    "templates/index.html": "<!-- HTML template -->\n",
    "model/model.pkl": "",  # This is just a placeholder; actual model should be added later
    "app.py": """from flask import Flask
from app.routes import *

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with content
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully.")
