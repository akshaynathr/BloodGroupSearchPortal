from flask.ext.mongoengine import  MongoEngine

db=MongoEngine()

class Details(db.Document):
	""" name:
	    bloodgroup
	    dept
	    gender
	    phoneno
	    year"""
	name=db.StringField(max_length=50,required=True)

	group=db.StringField(max_length=50,required=True)
	dept=db.StringField(max_length=50,required=True)
	gender=db.StringField(max_length=50,required=True)
	phoneno=db.StringField(max_length=50,required=True)
	year=db.StringField(max_length=50,required=True)
