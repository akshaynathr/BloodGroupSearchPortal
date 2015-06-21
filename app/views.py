from flask import Flask

from flask.ext.mongoengine import MongoEngine

from mongoengine import *
from flask import render_template,request

from models import Details,db
from pymongo import read_preferences


application=Flask(__name__)
application.config["MONGODB_SETTINGS"]={'db':'projectB'}

application.secret_key="akshaynathrprojectB"

db.init_app(application)
def _sort(Data):
	words=Data.split()
	return words


@application.route('/home')
@application.route('/')

def home():
	return render_template("Home.html")

@application.route('/home',methods=["POST"])
@application.route('/',methods=["POST"])
def Search():
	term=request.form['search']
	words=_sort(term)	
	List=Details.objects.filter(Q(group=words[0]) & Q(year=words[2]) & Q(dept=words[1]) )
	title="Students with Blood Group " + term
	return render_template('List.html',details=List,title=title)


def _save_Details(name,group,dept,gender,phone,year):
	
	if Details.objects(phoneno=phone).first() is  None:
		Detail=Details()
		Detail.name=name
		Detail.group=group
		Detail.dept=dept
		Detail.phoneno=phone
		if int(gender) is 1:	
			Detail.gender="Male"
		elif int(gender) is 2:
			Detail.gender="Female"
		else:
			print ("Error. Wrong Gender specified")
		Detail.year=year
		Detail.save()
		return "<h2 style='color:green'> Data Registered. </h2><h5><a href='EnterDetails'>Go back</a></h5>"
	return "<h2 style='color:red'>Error</h2><h2>Possibly a duplicate... </h2><h5><a href='EnterDetails'>Go back</a></h5>"

@application.route('/EnterDetails')
def details():
	return render_template("DetailsEntry.html") 


@application.route('/EnterDetails',methods=["POST"])
def submit():
	Name=request.form['name']
	Group=request.form['group']
	Dept=request.form['dept']
	Gender=request.form['gender']
	Year=request.form['year']	
	Phone=request.form['phone']	
	if Name and Group and Dept and Gender and Phone:
		message=_save_Details(Name,Group,Dept,Gender,Phone,Year)
		return message 
	return "Error!Please Fill correctly.<h5><a href='EnterDetails'>Go back</a>"

@application.route('/all')
def display_all():
	Detail=Details()
	AllList=Details.objects.all()
	title="List of all Blood Groups"
	return render_template("List.html",details=AllList,title=title)

@application.route('/delete')
def delete():
	return render_template("del.html")

@application.route('/delete',methods=["POST"])
def delete_user():
	phoneno=request.form['phoneno']
	User=Details.objects(phoneno=phoneno).first()
	if User is None:
		return "<h2 style='color:red'>No user match</h2><h5><a href='/delete'>Go back</a></h5>"
	User.delete()
	return "<h2 style='color:red'>Deleted User</h2>"
