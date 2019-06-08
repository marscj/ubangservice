服务器配置：

GIT 配置
1. ssh-keygen -t rsa -C 'mjc_cj@163.com'
2. cat ~/.ssh/id_rsa.pub
3. 在git新建sshkey

安装python3
1. sudo apt-get update
2. sudo apt-get install python3 python-dev python3-dev python3-venv libpq-dev build-essential uwsgi-plugin-python uwsgi-plugin-python3 

安装虚拟环境
1. python3 -m venv env
2. source bin/activate
3. pip install --upgrade pip

安装项目
1. mkdir src
2. git clone git@github.com:marscj/ubangservice.git
3. pip install -r requirements.txt
4. ./manage.py makemigrations
5. ./manage.py migrate
6. ./manage.py collectstatic
7. ./manage.py loaddata init_data.yaml
8. ./manage.py createsuperuser

NGINX + UWSGI 部署
1. sudo apt-get install nginx
2. sudo apt-get install uwsgi
3. pip install uwsgi
命令
$ uwsgi --ini uwsgi.ini
$ sudo nginx -s stop
$ sudo nginx -s reload
$ sudo nginx 
$ cat 
$ tail -f log.log
$ sudo ln -s /home/ubuntu/venv/src/ubangservice/ubangservice/nginx.conf /etc/nginx/sites-enabled/
$ sudo ln -s /home/ubuntu/venv/src/ubangservice/ubangservice/uwsgi.ini /etc/uwsgi/apps-enabled/

Redis配置
1. sudo apt-get install redis-server
启动
$ redis-server
检查
$ redis-cli ping  

celery配置
启动任务队列
$ sudo apt-get supervisor
$ su 
$ echo_supervisord_conf > /etc/supervisord.conf
$ sudo vim /etc/supervisord.conf
文件末尾添加
##################################################################################
[program:celery.worker]
command= /home/ubuntu/venv/bin/celery -A ubangservice worker -l info
directory=/home/ubuntu/venv/src/ubangservice
numprocs=1
autostart=true
autorestart=true
startretries=3
redirect_stderr=true
stdout_logfile=/var/log/celery/celery_worker_out.log

[program:celery.beat]
command= /home/ubuntu/venv/bin/celery -A ubangservice beat -l info
directory=/home/ubuntu/venv/src/ubangservice
numprocs=1
autostart=true
autorestart=true
startretries=3
redirect_stderr=true
stdout_logfile=/var/log/celery/celery_beat_out.log
##################################################################################
sudo supervisord -c /etc/supervisord.conf

开启任务队列
$ celery -A ubangservice worker -l info 
清除任务队列
$ celery -A ubangservice purge



