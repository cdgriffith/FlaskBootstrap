# FlaskBootstrap
Generic starting point for a standard flask project

Designed for:

* Python 3.6+ 
* Linux

Replace all <project_name> with your own project's name. 
(may be with our without the carrets)

Create your own config file at <project_name>.config.yaml 

Should contain the following items:

```yaml
env: production
host: 0.0.0.0
port: 8080 # Should match the one in project_name.nginx
session_secret: bad_secret  # make real one with os.urandom(32).hex()
```


Run the project:

```bash
pip install -r requirements.txt
python -m project_name
```

## Deploy for project_name

As on Ubuntu 18.04

As root:
```
apt update
apt install nginx python3-venv python3-pip apache2-utils -y
mkdir /var/log/<project_name>
addgroup <project_name>
adduser <project_name> <project_name>
htpasswd -c /etc/nginx/.htpasswd <admin_user>

# make the three directories of the current live site (src), backup duirng deploy (backup) and staged files for deployment (staging)

mkdir -p /opt/<project_name> /opt/<project_name>/src /opt/<project_name>/staging /opt/<project_name>/backup

# Copy project to /opt/<project_name>/src/

chown -R <project_name>:<project_name> /opt/<project_name>
sudo -u <project_name> bash -c "python3 -m venv /opt/<project_name>/venv"
sudo -u <project_name> bash -c "/opt/<project_name>/venv/bin/pip install -r /opt/<project_name>/src/requirements.txt --no-cache"

# copy SSL certificate to /etc/ssl/certs/<project_name>.crt
# copy SSL key to /etc/ssl/private/<project_name>.key

cp /opt/<project_name>/src/<project_name>.nginx /etc/nginx/sites-available/<project_name>
chown root:root /etc/nginx/sites-available/<project_name>
chmod 0644 /etc/nginx/sites-available/<project_name>
ln -s /etc/nginx/sites-available/<project_name> /etc/nginx/sites-enabled/<project_name>
rm /etc/nginx/sites-enabled/default

cp /opt/<project_name>/src/<project_name>.service /etc/systemd/system/<project_name>.service
chown root:root /etc/systemd/system/<project_name>.service
chmod 0755 /etc/systemd/system/<project_name>.service
systemctl daemon-reload
systemctl enable  /etc/systemd/system/<project_name>.service
systemctl start <project_name>.service

# Modify /etc/nginx/nginx.conf, add under http
# client_max_body_size 2M;

service nginx restart

```

## TODO 

* Put and test cache in /tmp