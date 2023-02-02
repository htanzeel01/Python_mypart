from config import app, db
from studentmodel import Student,Classroom
 
with app.app_context():
    db.drop_all()
    db.create_all()