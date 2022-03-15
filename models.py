from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "table"
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image=db.column(db.String())
    
    def __repr__(self) :
        return "{} is the title and {} is the description".format(self.title,self.description)
