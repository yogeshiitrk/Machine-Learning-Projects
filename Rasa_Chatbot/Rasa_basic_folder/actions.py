from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from flask import Flask
from flask_mail import Mail, Message
import os
from  city_check import check_location
from zomato_slots import results
from email_config import Config
from flask_mail_check import send_email

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price').strip()

		global restaurants

		restaurants = results(loc, cuisine, price)
		restaurants.drop_duplicates(inplace = True)
		top5 = restaurants.head(5)
		
		# top 5 results to display
		if len(top5)>0:
			response = 'Showing you top results:' + "\n"
			for index, row in top5.iterrows():
				response = response + str(row["restaurant_name"]) + ' (rated ' + row['restaurant_rating'] + ') in ' + row['restaurant_address'] + ' and the average budget for two people ' + str(row['budget_for2people'])+"\n"
		else:
			response = 'No restaurants found' 

		dispatcher.utter_message(str(response))

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		recipient = tracker.get_slot('emailid')

		top10 = restaurants.head(10)
		print("got this correct")
		send_email(recipient, top10)

		dispatcher.utter_message("Have a great day!")

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location').lower().strip()
		check = check_location(loc)
		return [SlotSet('valid_loc',check)]


