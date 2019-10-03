# 曼威C2M项目 MOCK-API服务 Django后端


### 1、创建虚拟环境

```
    cd /opt
    which python2.7
    virtualenv pyEnvMock --python=/usr/bin/python2.7 --no-site-packages
    virtualenv pyEnvMock --python=/Users/ywzhou/anaconda3/bin/python3.6  --no-site-packages

```ls

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

安装 uwsgi
```
    yum install python-devel mysql-devel zlib-devel openssl-devel
    pip install uwsgi
```

### 3、准备数据库

3.1 创建数据库，如果不和下面的一致需要修改setting.py
    名称：MockServer
    账号：root
    密码：123456
    编码：utf8mb4

3.2 同步数据库结构
```
    cd /opt/pyEnvMock/mainiway-django-mock
    python manage.py migrate
```

3.3 创建超级管理员账号
```
    python manage.py createsuperuser
```

3.4 导入数据
```
    python data/import_mock_data.py
```

### 4、启动服务

```
    sh /opt/pyEnvMock/mainiway-django-mock/server/service.sh start env_dev
```

### 5、访问地址

    http://mw.mock.ywzhou.shop
    http://mw.mock.server.ywzhou.shop
    http://mw.mock.ywzhou.shop:9001


### BUG

错误1：

```
    Could not find an available JavaScript runtime
```

原因：
    直接在python虚拟环境中查看环境变量是这样的：

```
    python -c 'import os;print(os.environ["PATH"])'
    /Users/ywzhou/git/nvm/versions/node/v10.15.1/bin:/Users/ywzhou/Desktop/CODE/DRF/py27env/bin:/Users/ywzhou/anaconda3/bin:/Library/Frameworks/Python.framework/Versions/3.6/bin:/Library/Frameworks/Python.framework/Versions/3.5/bin:/usr/local/mysql/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

    而在execjs中是这样的：

```
    '/Users/ywzhou/Desktop/CODE/DRF/py27env/bin:/usr/bin:/bin:/usr/sbin:/sbin'
```

解决：
    settings.py中手动设定环境变量PATH：

```
    os.environ['PATH'] = '/usr/bin:' + os.environ['PATH']
```

错误2：

```
    list index out of range
```

设置setting.py中的DEBUG=False