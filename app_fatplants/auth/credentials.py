import yaml
import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("place") == "docker":
    path = "/app/"
else:
    path = "/home/scd2z/fatplants/app_fatplants/"


with open(path + "config.yaml") as file:
    yaml_file = yaml.load(file, Loader=yaml.FullLoader)
    db = yaml_file["database"]


db_credentials = db
