## Addit

---

A simple webapp app to show and search saved quotes,
like the ones from IRC

- Authentication needed to view quotes
- REST API with tokens for easy bot integration
- Mobile first design, dark mode
- Web Manifest for a snazzy install to phone home screen

---
### Deployment
1. copy `.env-example` to `.env` and change settings needed for deployment
2. copy `app/.env-example` to `app/.env` and change settings needed for the app
3. `docker compose build`
4. `docker compose run --rm app python3 manage.py migrate` to initialize the db
5. `docker compose run --rm app python3 manage.py createsuperuser` to create the superuser
6. `docker compose run --rm app python3 manage.py collectstatic --no-input` to get static files in the correct places
7. `docker compose up -d` to deploy to localhost

### Tests
Includes some django testing
1. `docker compose run --rm app bash`
2. `python3 manage.py test`
