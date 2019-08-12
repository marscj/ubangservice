服务器配置：

# GIT 配置
$ ssh-keygen -t rsa -C 'mjx_cj@163.com'
$ cat ~/.ssh/id_rsa.pub
$ 在git新建sshkey
5. admin admin123

# 安装python3
$ sudo apt-get update
$ sudo apt-get install python3 python-dev python3-dev python3-venv libpq-dev 
<!-- build-essential uwsgi-plugin-python uwsgi-plugin-python3  -->

# 安装虚拟环境
$ python3 -m venv venv
$ source bin/activate
$ pip install --upgrade pip

# PostgreSQL Linux 安装与配置
$ sudo apt-get install postgresql postgresql-contrib
$ sudo su - postgres
$ psql
$ CREATE DATABASE db;
$ CREATE USER admin WITH PASSWORD 'admin123';
$ GRANT ALL PRIVILEGES ON DATABASE db TO admin;
# PostgreSQL Mac 安装与配置
$ brew install postgresql
$ initdb /usr/local/var/postgres
$ pg_ctl -D /usr/local/var/postgres -l logfile start
$ createuser admin -P
$ createdb db
$ psql db
$ GRANT ALL PRIVILEGES ON DATABASE db TO admin;
删除数据库
$ DROP DATABASE dbname;


# Redis Linux 安装与配置
$ sudo apt-get install redis-server
启动
$ redis-server
检查
$ redis-cli ping  
# Redis mac 安装与配置
$ brew install redis
后台运行
$ brew services start redis 

# 安装项目
$ mkdir src
$ git clone git@github.com:marscj/ubangservice.git
$ pip install -r requirements.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py collectstatic
$ ./manage.py loaddata init_data.yaml
$ ./manage.py createsuperuser

# NGINX + UWSGI Linux 部署
$ sudo apt-get install nginx
$ sudo apt-get install uwsgi
测试
$ uwsgi --ini uwsgi.ini
$ sudo nginx -s stop
$ sudo nginx -s reload
$ sudo nginx 
$ cat 
$ tail -f log.log
制作软链
$ sudo ln -s /home/ubuntu/ubangservice/ubangservice/nginx.conf /etc/nginx/sites-enabled/
$ sudo ln -s /home/ubuntu/ubangservice/ubangservice/uwsgi.ini /etc/uwsgi/apps-enabled/
$ sudo rm -rf /etc/nginx/sites-enabled/default
$ sudo rm -rf /etc/uwsgi/apps-enabled/default

# Celery Linux 配置
启动任务队列
$ sudo apt-get install supervisor
$ sudo passwd
$ su 
$ echo_supervisord_conf > /etc/supervisor/conf.d/supervisord.conf
$ sudo vim /etc/supervisor/conf.d/supervisord.conf
文件末尾添加
--------------------------------------------------------------------------------
[program:celery.worker]
command= /home/ubuntu/venv/bin/celery -A ubangservice worker -l info
directory=/home/ubuntu/ubangservice
numprocs=1
autostart=true
autorestart=true
startretries=3
redirect_stderr=true
;stdout_logfile=/var/log/celery/celery_worker_out.log

[program:celery.beat]
command= /home/ubuntu/venv/bin/celery -A ubangservice beat -l info
directory=/home/ubuntu/ubangservice
numprocs=1
autostart=true
autorestart=true
startretries=3
redirect_stderr=true
;stdout_logfile=/var/log/celery/celery_beat_out.log
--------------------------------------------------------------------------------

sudo supervisord -c /etc/supervisor/conf.d/supervisord.conf

开启任务队列
$ celery -A ubangservice worker -l info 
清除任务队列
$ celery -A ubangservice purge

# 数据库迁移
$ python manage.py dumpdata > db.json
<!-- Change the database settings to new database such as of MySQL / PostgreSQL. -->
$ python manage.py migrate
$ python manage.py shell 
<!-- Enter the following in the shell -->
$ from django.contrib.contenttypes.models import ContentType
$ ContentType.objects.all().delete()
$ python manage.py loaddata db.json
