# 曼威C2M项目 MOCK-API服务 Django后端


### 1、创建虚拟环境

```
    cd /opt
    which python2.7
    virtualenv pyEnvMock --python=/usr/bin/python2.7 --no-site-packages
    virtualenv pyEnvMock --python=/Users/ywzhou/anaconda3/bin/python3.6  --no-site-packages

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

错误3:

跨域问题
在nginx.confg文件中配置
```
        add_header  Access-Control-Allow-Headers '*';
```




# 使用docker方式部署

前提：
    安装docker及mysql redis容器服务

### 1、MockServer后台

拉取项目

```
	mkdir -p /docker/MockServer/{MockServer,web,logs,conf}
	cd /docker/MockServer/MockServer
	git init
	git pull https://github.com/ywzhou123/mainiway-django-mock.git
```

编译容器

```
    sudo docker build -t django-mock .
    sudo sh start.sh
```

导入sql数据

```
    docker cp data/MockServer.sql mysql:/MockServer.sql
    docker exec -it mysql bash
    mysql -uroot -p123456
    >CREATE DATABASE  `MockServer` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    >use MockServer;
    >source MockServer.sql;
```

访问：
http://ip:8004/snippets/

部署前台页面:
    如果不是部署在同一台服务器，或者后端不是8004端口，需要修改webpack.config.js中的ip和端口
    将打包生成的dist目录下的内容上传到/docker/MockServer/web
    不想打包，可以直接使用前端项目中的dist目录

[项目仓库](https://github.com/ywzhou123/mainiway-react-mock)



```
vi /etc/nginx/conf.d/mock.conf
server {
    listen      80;

    server_name mock.ywzhou.shop;
    charset     utf-8;

    client_max_body_size 20M;

    location    / {
        add_header  Access-Control-Allow-Headers '*';
        root    /docker/MockServer/web;
        index   index.html;
    }
}
systemctl reload nginx
```

http://mock.ywzhou.shop
