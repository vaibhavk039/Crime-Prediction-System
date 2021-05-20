import numpy as np
from flask import Flask, render_template,request
import pickle
import pandas as pd
import io
from geopy.geocoders import Nominatim
from datetime import datetime,date,time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
	geolocator = Nominatim(user_agent="crime-dataset")
	if request.method=='POST':
		candidate=request.form
		loc=candidate['name']
		print(type(loc))
		time=candidate['time']
		ct = datetime.now()
		cd=date.today()
		location=geolocator.geocode(loc)
		lat=round(location.latitude,2)
		lon=round(location.longitude,2)
		p=[ct.month,ct.day,ct.hour,cd.timetuple().tm_yday,lat,lon]
		final_features=[np.array(p)]
		pred=model.predict(final_features)		
		text=pred 
		if(1 in pred[0]):
			t=list(pred[0]).index(1)
			crimes=['Murder','Rape','Kidnapping','Speeding','Domestic Violence','Robbery']
			text=str(crimes[t])+" is a prominent crime in " + str(loc)
		else:
			text='No prominent crime.'
		return render_template('contact.html',pt=text)

	return render_template('contact.html')

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/city_plot')
def city_plot():
	return render_template('city_plot.html')

@app.route('/year_wise')
def year_wise():
	return render_template('year_wise.html')

@app.route('/month_wise')
def month_wise():
	return render_template('month_wise.html')

@app.route('/auto_theft')
def auto_theft():
	return render_template('auto_theft.html')

@app.route('/rape')
def rape():
	return render_template('rape.html')

@app.route('/geo')
def geo():
	return render_template('geo.html')

@app.route('/total_crime')
def total_crime():
	return render_template('total_crime.html')

@app.route('/crime_plot')
def crime_plot():
	return render_template('crime_plot.html')

@app.route('/register',methods=['POST','GET'])
def register():
	if request.method=='POST':
		candidate=request.form
		name=candidate['name']
		email=candidate['email']
		city=candidate['city']
		state=candidate['state']
		crime=candidate['crime']
		time=candidate['time']
		message="Thank You for your valuable contribution."
		return render_template('register.html',message=message)
	return render_template('register.html',message='')






