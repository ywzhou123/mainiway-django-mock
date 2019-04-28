#!/bin/bash

ENV="/opt/pyEnvMock"

ROOT="${ENV}/mainiway-django-mock"

SERVER="${ROOT}/server/$2"

CONFS="${ROOT}/server/confs"

USERNAME="admin"

PASSWORD="s8F1#0cD2#d3ca"

install(){
    $ENV/bin/pip install -r $ROOT/requirements.txt
}

reload(){
#    cp -f $CONFS/nginx.conf /etc/nginx/nginx.conf
#    cp -f $SERVER/config.py $ROOT/FarmPlatform/config.py
    cp -f $SERVER/nginx.conf /etc/nginx/conf.d/nginx_django_mock.conf
}

usage() {
    echo "Usage: sh service.sh [install|start|stop|reload|restart|status|killsuper] [env_dev|env_test|env_pre|env_production|env_demo]"
    exit 1
}

is_exist(){
    pid=`ps -ef|grep 'supervisord -c /opt/pyEnvMock' |grep -v grep|awk '{print $2}' `
    if [ -z "${pid}" ];  then
        return 1
    else
        return 0
    fi
}

start(){
    is_exist
    if [ $? -eq "0" ];  then
        echo "supervisord is already running. pid=${pid} ."
    else
        supervisord -c $CONFS/supervisor.conf
    fi
    systemctl start nginx
}

stop(){
    is_exist
    if [ $? -eq "0" ];  then
        supervisorctl -u ${USERNAME} -p ${PASSWORD} shutdown
    else
        echo "supervisord is not running"
    fi
    systemctl stop nginx
}

status(){
    is_exist
    if [ $? -eq "0" ]; then
        echo "supervisord is running. Pid is ${pid}"
    else
        echo "supervisord is NOT running."
    fi
    systemctl status nginx
}

restart(){
    is_exist
    if [ $? -eq "0" ]; then
        supervisorctl -u ${USERNAME} -p ${PASSWORD} restart all
        if [ $? -ne "0" ]; then
            killsuper && supervisord -c $CONFS/supervisor.conf
        fi
    else
        supervisord -c $CONFS/supervisor.conf
    fi
    systemctl restart nginx
}

killsuper(){
    killall -9 supervisord
    killall -9 $ENV/bin/uwsgi
    killall -9 $ENV/bin/python
}

case "$2" in
    "env_dev" | "env_test" | "env_pre"| "env_production" | "env_demo")
        ;;
    *)
        usage
        ;;
esac

case "$1" in
    "install")
        install
        ;;
    "start")
        reload
        start
        ;;
    "stop")
        stop
        ;;
    "status")
        status
        ;;
    "reload")
        reload
        ;;
    "restart")
        reload
        restart
        ;;
    "killsuper")
        killsuper
        ;;
    *)
        usage
        ;;
esac