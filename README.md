# PlantegrA

CRM and Resource Management for IntegrA

## Requirements

- `docker` and `docker-compose`.
You can also set it up without docker.
If you do please document the changes which are required (such as setting up a database).
- `python >= 3.6`
- `pip` or some other way to get the requirements in `requirements.txt`

## Development Setup

1. Clone Repository
2. Optional: Set up virtual environment with `virtualenv -p python3 <virtuelenv dir (e.g .env/)>` and activate it with `source <env dir>/bin/activate`.
3. Copy `plantegra/local_settings.py.template` to `plantegra/local_settings.py` and set all settings inside it.
4. Start docker-compose.dev.yml for running a PostgreSQL server: `docker-compose -f docker-compose.dev.yml up` 
(Alternatively you can run your DB the way you want (e.g. MySQL or SQLite), but you'll have to change the `DATABASES` setting, which is defined in [settings](plantegra/settings.py).
Please do not commit these changes. Instead overwrite them in the [local settings](plantegra/local_settings.py), which is ignored by Git).
5. Install requirements `pip install -r requirements.txt`
6. Migrate Database Schema `python manage.py migrate`
7. Create Super User: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`

## Reset DB data

1. Shutdown PostgreSQL container and remove: `docker-compose -f docker-compose.dev.yml down`
2. Delete db volume (your volume may be named otherwise, depending on the project folder): `docker volume rm plantegra_dbdata`
3. Start PostgreSQL container again: `docker-compose -f docker-compose.dev.yml up`
