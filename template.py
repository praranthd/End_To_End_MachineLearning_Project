import os
from pathlib import Path
import logging

project_name = "datascience"

# Configure logging

logging.basicConfig(
level=logging.INFO,
format="[%(asctime)s: %(levelname)s: %(message)s]"
)

list_of_files = [
".github/workflows/.gitkeep",

# Source code
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/utils/common.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/entity/config_entity.py",
f"src/{project_name}/constants/__init__.py",

# Configuration
"config/config.yaml",
"params.yaml",
"schema.yaml",

# FastAPI backend
"api/__init__.py",
"api/main.py",
"api/routes.py",
"api/schemas.py",

# Streamlit frontend
"streamlit_app/Home.py",
"streamlit_app/pages/1_Prediction.py",
"streamlit_app/utils.py",

# Project files
"main.py",
"Dockerfile",
"requirements.txt",
"setup.py",
".gitignore",

# Research
"research/research.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    try:
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(
            f"Directory created or already exists: {filedir}"
        )

    # Create the file if it does not exist
        if not filepath.exists():
            with open(filepath, "w") as f:
                pass
            logging.info(f"Created file: {filepath}")

        else:
            logging.info(f"File already exists: {filepath}")

    except Exception as e:
        logging.error(f"Error creating {filepath}: {e}")
        raise
