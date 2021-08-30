import json
import csv


city_dict = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer',
'Aligarh','Allahabad','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi',
'Bhopal','Bhubaneswar','Bikaner','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad',
'Durg-Bhilai Nagar','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
'Gurgaon','Guwahati‚ Gwalior','Hubli-Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur',
'Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi','Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool',
'Lucknow','Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik',
'Nellore','Noida','Palakkad','Patna','Pondicherry','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri',
'Solapur','Srinagar','Sultanpur','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruppur','Ujjain','Vijayapura',
'Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Warangal']

city_dict = [x.lower() for x in city_dict]
def getAllCities():
	cities =[]
	with open('cities.csv', "r") as csvfile:
		reader = csv.reader(csvfile)
		cities = [row[0].lower().strip() for row in reader]
	return cities

def check_location(loc):
	print(loc)
	if loc not in getAllCities():
		return "notfound"
	elif loc not in city_dict:
		return "tier3"
	else:
		return "found"

		
		

