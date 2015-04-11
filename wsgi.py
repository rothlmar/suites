#!/usr/bin/python
import os

virtenv = os.environ.get('OPENSHIFT_PYTHON_DIR','') + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from suitetester import application

if __name__ == "__main__":
    application.run('0.0.0.0',5000)
