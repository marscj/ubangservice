服务器配置：

GIT 配置
1. ssh-keygen -t rsa -C 'mjc_cj@163.com'
2. cat ~/.ssh/id_rsa.pub
3. 在git新建sshkey

安装python3
1. sudo apt-get update
2. sudo apt-get install python3 python-dev python3-dev libpq-dev


安装虚拟环境
1. sudo apt-get install python3-venv
2. python3 -m venv env
3. source bin/activate
4. pip install --upgrade pip

安装项目
1. mkdir src
2. git clone git@github.com:marscj/ubangservice.git
3. pip install -r requirements.txt

NGINX + UWSGI 部署
1. sudo apt-get install nginx

