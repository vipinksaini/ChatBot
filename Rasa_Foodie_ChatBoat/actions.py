from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

global resrnt_df10
resrnt_df10 = pd.DataFrame()
		
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def filterRestOnBudget(self, userprice, allRestnts):
		rangeMin = 0
		rangeMax = 1000

		if str(userprice).isdigit():
			price = int(userprice)

			if price == 1:
				rangeMax = 300
			elif price == 2:
				rangeMin = 301
				rangeMax = 700
			elif price == 3:
				rangeMin = 700
			elif price < 300:
				rangeMax = 299
			elif price < 300 and price >= 700:
				rangeMin = 300
				rangeMax = 699
			else:
				rangeMin = 700
		else:
			# default budget 
			rangeMin = 300
			rangeMax = 700
			
		cols = ['restaurant name', 'restaurant address', 'avg. budget for two', 'zomato rating']
		resrnt_df10 = pd.DataFrame()
		resrnt_df = pd.DataFrame(columns = cols)
		for restaurant in allRestnts['restaurants']:
				curr_res = {'zomato rating':restaurant['restaurant']["user_rating"]["aggregate_rating"],'restaurant name':restaurant['restaurant']['name'],'restaurant address': restaurant['restaurant']['location']['address'], 'avg. budget for two': restaurant['restaurant']['average_cost_for_two']}		
				if (curr_res['avg. budget for two'] >= rangeMin) and (curr_res['avg. budget for two'] <= rangeMax):						
						resrnt_df.loc[len(resrnt_df)] = curr_res
		resrnt_df = resrnt_df.sort_values(['zomato rating','avg. budget for two'], ascending=[False,True])
		global resrnt_df10
		resrnt_df10 = resrnt_df.head(10)
		resrnt_df10 = resrnt_df10.reset_index(drop=True)
		resrnt_df10.index = resrnt_df10.index.map(str)
		
		if len(resrnt_df10) <= 0:
			response = "Found 0 restaurants in given price range"
		else:
			response = "Showing you top rated restaurants: \n"
			for index, row in resrnt_df10[:5].iterrows():
				response=response+ index + ". Found \""+ row['restaurant name']+ "\" in "+ row['restaurant address']+" has been rated "+ row['zomato rating']+"\n"
					
		return response
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"54a2af9ddc7a097a6dce95baa3666da1"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]		
		cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			response = self.filterRestOnBudget(price, d)				
		
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

		
		
cities = ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai", "Pune", 
						"Agra", "Ajmer", "Aligarh", "Amravati", "Amritsar", "Asansol", "Aurangabad", "Bareilly",
						"Belgaum", "Bhavnagar", "Bhiwandi", "Bhopal", "Bhubaneswar", "Bikaner", "Bokaro Steel City",
						"Chandigarh", "Coimbatore", "Cuttack", "Dehradun", "Dhanbad", "Durg Bhilai Nagar", "Durgapur",
						"Erode", "Faridabad", "Firozabad", "Ghaziabad", "Gorakhpur", "Gulbarga", "Guntur", "Gurgaon",
						"Guwahati", "Gwalior", "Hubli-Dharwad", "Indore", "Jabalpur", "Jaipur", "Jalandhar", "Jammu",
						"Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Kannur", "Kanpur", "Kakinada", "Kochi",
						"Kottayam", "Kolhapur", "Kollam", "Kota", "Kozhikode", "Kurnool", "Lucknow", "Ludhiana",
						"Madurai", "Malappuram", "Mathura", "Goa", "Mangalore", "Meerut", "Moradabad", "Mysore",
						"Nagpur", "Nanded", "Nashik", "Nellore", "Noida", "Palakkad", "Patna", "Pondicherry",
						"Prayagraj", "Raipur", "Rajkot", "Rajahmundry", "Ranchi", "Rourkela", "Salem",
						"Sangli", "Siliguri", "Solapur", "Srinagar", "Sultanpur", "Surat", "Thiruvananthapuram",
						"Thrissur", "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Ujjain", "Bijapur", "Vadodara",
						"Varanasi", "Vasai-Virar City", "Vijayawada", "Visakhapatnam", "Warangal"]
cities = [x.lower() for x in cities]
# Check if the location exists.  utter not found.
class ActionValidateLoc(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		
		if city.lower() in cities:
			return [SlotSet('location',loc)]
		else:			
			return [SlotSet('location',None)]		
	
class ActionSentEmail(Action):
	def name(self):
		return 'action_SentEmail'
		
	def run(self, dispatcher, tracker, domain):	
		email = tracker.get_slot('email')
		gmail_user = 'sent@gmail.com'  
		gmail_password = '5october'		
		to = str(email)
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Foodie friend here"
		msg['From'] = gmail_user
		msg['To'] = to
		global resrnt_df10
		if len(resrnt_df10) <= 0:
			dispatcher.utter_message("Sorry, we could not find restaurants")
		else:			
			resrnt_df10 = resrnt_df10.reset_index(drop=True)
			resrnt_df10.index = resrnt_df10.index.map(str)
			html = """
			<html>
			<head>			
			</head>
			<body>
			<p>Hi!</p>
			<p>Foddie friend here , Please find the resturants below.</p>			
			"""
			html = html+resrnt_df10.to_html()
			resrnt_df10 = pd.DataFrame()
			part2 = MIMEText(html, 'html')
			msg.attach(part2)
			try:
				server = smtplib.SMTP_SSL('smtp.gmail.com',465)
				server.ehlo()
				server.login(gmail_user, gmail_password)			
				server.sendmail(gmail_user, to, msg.as_string())
				server.close()
			except:
				dispatcher.utter_message(email)
		return [SlotSet("email", None), SlotSet("price", None), SlotSet("cuisine", None), SlotSet("location", None)]

