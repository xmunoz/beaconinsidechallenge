import os
import sys

APP_HOME = "/home/cristina/public/xmunoz/main/web/caesar"

activate_this = os.path.join(APP_HOME, "venv_caesar/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, APP_HOME)
os.chdir(APP_HOME)

from crypto_app.routes import app as application
