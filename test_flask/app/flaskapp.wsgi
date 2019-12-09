import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/flask/test_flask")  

from app import app as application
application.secret_key = '2ad3c3ea1ac24c2fbc33bf9ee5a3d77c'
