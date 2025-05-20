from dotenv import load_dotenv
import os

# Charger les variables depuis le fichier .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
