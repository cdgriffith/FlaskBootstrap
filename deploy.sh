#!/usr/bin/env bash
SET -e
rsync -avzh --exclude=staging/ --exclude=venv/ --exclude=<project_name>/cache/ --exclude=backup/ --exclude=config.yaml /opt/<project_name>/src/ /opt/<project_name>/backup/
rsync -avzh --exclude=staging/*config.yaml --exclude=*config.yaml --exclude=*.log --exclude=staging/*.log /opt/<project_name>/staging/ /opt/<project_name>/src/
chown -R <project_name>:<project_name> /opt/<project_name>/src/
sudo -u <project_name> bash -c "/opt/onfido_upload/venv/bin/pip install -r /opt/onfido_upload/src/requirements.txt --no-cache"
service <project_name> restart

