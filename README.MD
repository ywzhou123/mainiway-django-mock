# 曼威C2M项目 MOCK-API服务 Django后端

### 1、让MySQL支持中文

```
    vi /etc/mysql/my.cnf
        [mysqld]
        character-set-server=utf8
        [client]
        default-character-set=utf8
```

### 2、修改已经有的table的编码:
```
        mysql -u root -p
        > alter table table_name convert to character set utf8;
```

### 3、创建虚拟环境

```
    cd /opt
    which python2.7
    virtualenv pyEnvMock --python=/usr/bin/python2.7 --no-site-packages

```

### 4、下载代码安装软件包

```
    cd /opt/pyEnvMock
    git clone git@github.com:ywzhou123/mainiway-django-mock.git
    source bin/activate
    pip install -r mainiway-django-mock/requirements.txt
```

安装node软件包，前提是系统安装了node和npm
```
    npm install mockjs
```

### 5、导入JSON备份数据

在虚拟环境中执行
```
    python data/import_mock_data.py
```

### 6、其他相关命令

```
    pip freeze > requirements.txt
    pip install -r requirements.txt
    vi MockServer/setting.py
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    python manage.py collectstatic
```