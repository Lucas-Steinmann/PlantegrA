# PlantegrA

CRM and Resource Management for IntegrA

## Development Setup

1. Clone Repository
2. Copy `plantegra/local_settings.py.template` to `plantegra/local_settings.py` and set all settings inside it.
3. Start docker-compose.dev.yml for running a PostgreSQL server: `docker-compose -f docker-compose.dev.yml up` 
(Alternatively you can run your DB the way you want (e.g. MySQL or SQLite), but you'll have to change the `DATABASES` setting, which is defined in [settings](plantegra/settings.py).
Please do not commit these changes. Instead overwrite them in the [local settings](plantegra/local_settings.py), which is ignored by Git).
4. Install requirements `pip install -r requirements.txt`
5. Migrate Database Schema `python manage.py migrate`
6. Create Super User: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## Reset DB data

1. Shutdown PostgreSQL container and remove: `docker-compose -f docker-compose.dev.yml down`
2. Delete db volume (your volume may be named otherwise, depending on the project folder): `docker volume rm plantegra_dbdata`
3. Start PostgreSQL container again: `docker-compose -f docker-compose.dev.yml up`
