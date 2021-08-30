## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"valid_loc": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_sendmail
* affirm{"emailid": "yrajput@vmware.com"}
    - slot{"emailid": "yrajput@vmware.com"}
    - action_send_email
    - utter_sent_email

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"valid_loc": "tier3"}
    - utter_do_not_operate
* restaurant_search{"location": " Allahabad"}
    - slot{"location": " Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_sendmail
* affirm{"emailid": "yrajput@vmware.com"}
    - slot{"emailid": "yrajput@vmware.com"}
    - action_send_email
    - utter_sent_email

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": " Kolkata"}
    - slot{"location": " Kolkata"}
    - action_validate_location
    - slot{"valid_loc": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* restaurant_search{"emailid": "yrajput@vmware.com"}
    - slot{"emailid": "yrajput@vmware.com"}
    - utter_sent_email

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"valid_loc": "notfound"}
    - utter_location_not_found
* restaurant_search{"location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - action_validate_location
    - slot{"valid_loc": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* restaurant_search{"emailid": "yrajput@vmware.com"}
    - slot{"emailid": "yrajput@vmware.com"}
    - action_send_email
    - utter_sent_email

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": " Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": " Chandigarh"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_sendmail
* deny
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"valid_loc": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexica"}
    - slot{"cuisine": "Mexica"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_sendmail
* deny
    - utter_goodbye
## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"valid_loc": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_sendmail
* restaurant_search{"emailid": "yrajput@vmware.com"}
    - slot{"emailid": "yrajput@vmware.com"}
    - action_send_email
    - utter_sent_email

## interactive_story_6
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"valid_loc": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_sendmail
* affirm{"emailid": "yrajput@vmware.com"}
    - slot{"emailid": "yrajput@vmware.com"}
    - action_send_email
    - utter_sent_email

## interactive_story_5
* restaurant_search{"cuisine": "chinese", "location": " Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": " Chandigarh"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_sendmail
* deny
    - utter_goodbye