#!/bin/bash
set -e


NEW_DB=callservice
NEW_USER=callservice
NEW_PASSWORD=callservice
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER ${NEW_USER} WITH PASSWORD '${NEW_PASSWORD}';
    ALTER ROLE ${NEW_USER} SET client_encoding TO 'utf8';
    ALTER ROLE ${NEW_USER} SET default_transaction_isolation TO 'read committed';
    ALTER ROLE ${NEW_USER} SET timezone TO 'UTC';
    CREATE DATABASE ${NEW_DB} WITH OWNER ${NEW_USER};
    GRANT ALL PRIVILEGES ON DATABASE ${NEW_DB} to ${NEW_USER};
EOSQL
