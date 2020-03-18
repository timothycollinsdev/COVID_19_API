# COVID_19_API

This is a scrapper which can get data from "worldometers" websit
https://www.worldometers.info/coronavirus/


To setup simply:
- clone the Repo 
- pip install -r requirements.txt
- python manage.py migrate --settings=COVID_19_API.settings.local
- python manage.py populate_db

## APIs Exposed
localhost:8000/api/v1/all/
