#!/bin/bash
ENV="/opt/py3env"

SERVER="${ENV}/FarmPlatform/server/env_dev"

#$ENV/bin/pip install -r $ENV/FarmPlatform/requirements.txt

cp -f $SERVER/nginx.conf /etc/nginx/conf.d/nginx_django.conf
cp -f $SERVER/super_uwsgi.conf /etc/supervisor/conf.d/super_uwsgi.conf
cp -f $SERVER/super_celery.conf /etc/supervisor/conf.d/super_celery.conf

systemctl restart nginx

killall -9 supervisord

killall -9 uwsgi

supervisord -c /etc/supervisor/supervisor.conf

#$ENV/bin/uwsgi --ini $SERVER/uwsgi.ini &
#supervisorctl -c /etc/supervisor/conf.d/super_uwsgi.conf restart uwsgi
#supervisorctl -c /etc/supervisor/conf.d/super_celery.conf restart celery