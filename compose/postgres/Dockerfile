FROM postgres:9.6

COPY ./backup.sh /usr/local/bin/backup
RUN chmod +x /usr/local/bin/backup

COPY ./restore.sh /usr/local/bin/restore
RUN chmod +x /usr/local/bin/restore

COPY ./list-backups.sh /usr/local/bin/list-backups
RUN chmod +x /usr/local/bin/list-backups

COPY ./init-user-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
RUN chmod +x /docker-entrypoint-initdb.d/init-user-db.sh
