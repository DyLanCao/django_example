# uwsig使用配置文件启动
[uwsgi]
# 项目目录
chdir=/Users/caoyin/Documents/igihub/django/django_example/helloapp/
# 指定项目的application
module=helloapp.wsgi:application
# 指定sock的文件路径       
socket=/Users/caoyin/Documents/igihub/django/django_example/helloapp/script/uwsgi.sock
# 进程个数       
workers=5
pidfile=/Users/caoyin/Documents/igihub/django/django_example/helloapp/script/uwsgi.pid
# 指定IP端口       
socket=127.0.0.1:8008
# 指定静态文件
#static-map=/static=/opt/proj/teacher/static
# 启动uwsgi的用户名和用户组
uid=root
gid=root
# 启用主进程
master=true
# 自动移除unix Socket和pid文件当服务停止的时候
vacuum=true
# 序列化接受的内容，如果可能的话
thunder-lock=true
# 启用线程
enable-threads=true
# 设置自中断时间
harakiri=30
# 设置缓冲
post-buffering=4096
# 设置日志目录
daemonize=/Users/caoyin/Documents/igihub/django/django_example/helloapp/script/uwsgi.log
