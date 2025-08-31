import os
from flask import Flask, send_from _directory from flask_cors import CORS
from src. models. user import db
as user
db
from
sic. models government_entities
import db
from src. routes. user import user_bp from src. routes. chatbot import chatbot_bp
app = Flask name
static _folder='static)
CORS (app)
app.register_blueprint (user_bp, url_prefix='7api')
app register blueprint (chatbot_bp, url _prefix='7api')
# Database configuration
app configl 'SQLALCHEMY_DATABASE_URI'
】= f"sqlite:///
{os. path. join(os.path.dirname(file _), 'database', 'app.db' )}"
app.configl'SQLALCHEMY_TRACK _MODIFIC
ATIONS' ] = False
db. init_app(app) with app.app_context(): db.create_all()
Capp. route ('/', defaults={'path' :
11})
Capp. route ('/<path:path>') def serve_static(path) :
if path != "
and
os.path.exists(os.path.join(app.stat ic_folder, path)) :
return
send_from_directory (app.static_folde
I, path) else:
return
send_from_directory (app.static_folde
I ,
'index.html' )
if
name_
main
port =
int(os.environ.get ( 'PORT', 5000) )
app. run (host=' 0.0.0.0'
port=port, debug=False)