activate_this = '/var/www/html/flask/test_flask/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))



import site
import sys
import os
prev_sys_path = list(sys.path)
site.addsitedir('/var/www/html/flask/test_flask/venv/Lib/site-packages/') # thrid-party package
reload(sys)
sys.setdefaultencoding('utf-8')
'''
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
        sys.path[:0] = new_sys_path
'''
sys.path.insert(0,"/var/www/html/flask/test_flask")


  

from app import app as application
#from manage import application
application.secret_key = '2ad3c3ea1ac24c2fbc33bf9ee5a3d77c'


