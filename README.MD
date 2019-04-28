# 曼威C2M项目 MOCK-API服务 Django后端


### 1、创建虚拟环境

```
    cd /opt
    which python2.7
    virtualenv pyEnvMock --python=/usr/bin/python2.7 --no-site-packages
```

进入虚拟环境，以下pip安装都需要在虚拟环境中执行
```
    source bin/activate
```

### 2、下载代码安装软件包

```
    cd /opt/pyEnvMock
    git clone git@github.com:ywzhou123/mainiway-django-mock.git
    pip install -r mainiway-django-mock/requirements.txt
```

安装node软件包，前提是系统安装了node和npm
```
    npm install mockjs
```


### 3、准备数据库

创建数据库，如果不和下面的一致需要修改setting.py
    名称：MockServer
    账号：root
    密码：123456
    编码：utf8mb4

同步数据库结构
```
    cd /opt/pyEnvMock/mainiway-django-mock
    python manage.py migrate
```

创建超级管理员账号
```
    python manage.py createsuperuser
```

导入数据
```
    python data/import_mock_data.py
```

### 4、启动服务

```
    sh /opt/pyEnvMock/mainiway-django-mock/server/service.sh start env_dev
```