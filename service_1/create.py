from application import db
from application.models import history


db.drop_all()
db.create_all()