from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy ( )
class User (db. Model) :
id = db. Column (db. Integer,
primary_key=True)
username =
db. Column (db. String ( 80), unique-True, nullable=False)
email =
db. Column (db. String ( 120), unique=True, nullable=False)
created at =
db. Column (db. DateTime, default=db. func. current_timestamp ())
def to dict (self):
return {
'id': self.id,
'username'
self. username,
email': self .email,
'created at':
self. created_at. isoformat () if self. created _at else None