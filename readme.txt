让MySQL支持中文
    /etc/mysql/my.cnf
        [mysqld]
        character-set-server=utf8
        [client]
        default-character-set=utf8
    修改已经有的table的编码:
        alter table table_name convert to character set utf8;

brew install mysql

sudo ln -s /usr/local/mysql/bin/* /usr/bin
vi ~/.bash_profile
export PATH="/usr/local/mysql/bin:${PATH}"

pip install ipython --user -U
sudo pip install djangorestframework MySQL-python django-cors-headers django-filter PyExecJS


sudo pip install MySQL-python

python manage.py createsuperuser
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver

 vi /Library/LaunchDaemons/com.oracle.oss.mysql.mysqld.plist
mysqld_safe --skip-grant-tables --skip-networking &

sudo npm install mockjs

导入JSON数据
python manage.py shell
    from app.models import Snippet
    import os,json
    p=os.path.join(os.getcwd(),'mock.json')
    f=open(p,'r').read().decode('utf-8')
    for [k,v] in dict.items(json.loads(f)):
        try:
            snippet = Snippet.objects.get(url=k)
        except Snippet.DoesNotExist:
            snippet=Snippet(url=k,owner_id=1)
            for [k2,v2] in dict.items(v):
                if(k2=='data'):
                    snippet.code=json.dumps(v2)
                if(k2=='msg'):
                    snippet.title=v2
        snippet.save()


pip freeze > requirements.txt
pip install -r requirements.txt

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
python manage.py collectstatic