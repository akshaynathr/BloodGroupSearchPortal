from flask import Flask

from flask.ext.mongoengine import MongoEngine

from flask import render_template,request

from models import Details,db
from pymongo import read_preferences


application=Flask(__name__)
application.config["MONGODB_SETTINGS"]={'db':'projectB'}

application.secret_key="akshaynathrprojectB"

db.init_app(application)


@application.route('/home')
@application.route('/')

def home():
	return render_template("Home.html")

@application.route('/home',methods=["POST"])
@application.route('/',methods=["POST"])
def Search():
	term=request.form['search']
	List=Details.objects(group=term).all()
	print("")
	print(List)
	title="Students with Blood Group " + term
	return render_template('List.html',details=List,title=title)


def _save_Details(name,group,dept,gender,phone):
	Detail=Details()
	Detail.name=name
	Detail.group=group
	Detail.dept=dept
	Detail.phoneno=phone	
	Detail.gender=gender
	Detail.save()


@application.route('/EnterDetails')
def details():
	return render_template("DetailsEntry.html") 


@application.route('/EnterDetails',methods=["POST"])
def submit():
	Name=request.form['name']
	Group=request.form['group']
	Dept=request.form['dept']
	Gender=request.form['gender']
	Phone=request.form['phone']	
	if Name and Group and Dept and Gender and Phone:
		_save_Details(Name,Group,Dept,Gender,Phone)
		return "Done"
	return "Error!Please Fill correctly"

@application.route('/all')
def display_all():
	Detail=Details()
	AllList=Details.objects.all()
	title="List of all Blood Groups"
	return render_template("List.html",details=AllList,title=title)

@application.route('/delete')
def delete_user():
	return ''
