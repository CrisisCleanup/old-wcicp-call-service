WCICP Call Service
=============
:License: Apache Software License 2.0

Pre-Req
-----
* docker
* docker-compose

Setup
-----

- Clone repo
- cd repo
- docker-compose build
- docker-compose up -d
- http://localhost:8020 (API)
- Changes in the code base will autoreload API
- OpenAPI/Swagger endpoint - http://localhost:8020/calls-openapi
- Admin endpoint - http://localhost:8020/calls-admin/


Migrations (will auto-migrate on container startup)
-----
- docker-compose exec callservice ./manage.py migrate

Fixtures
-----
- docker-compose exec callservice ./manage.py loaddata initial

Bash (CWD - app root)
-----
- docker-compose exec callservice bash
