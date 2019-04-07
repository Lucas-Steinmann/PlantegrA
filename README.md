# PlantegrA

CRM

## Development Setup

1. Clone Repository
2. Start docker-compose.dev.yml with Postgresql: `docker-compose -f docker-compose.dev.yml`
3. Migrate Database Schema `python manage.py migrate`
4. Create Super User: `python manage.py createsuperuser`
5. Run server: `python manage.py runserver`