# from studentmodel import Student
# from datetime import datetime

# from marshmallow_sqlalchemy import fields

# from config import db, ma



# class Classroom(db.Model):
#     __tablename__ = "classroom"
#     id = db.Column(db.Integer, primary_key=True)
   
#     classname = db.Column(db.String, nullable=False)
#     student = db.relationship(
#         Student,
#         backref="classroom",
#         cascade="all, delete, delete-orphan",
#         single_parent=True,
#         order_by="desc(Note.timestamp)",
#     )

# class ClassSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Classroom
#         load_instance = True
#         sqla_session = db.session
#         include_fk = True

# class_schema = ClassSchema()