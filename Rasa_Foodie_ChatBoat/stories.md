## Generated Story -5498761941985698037
* greet
* greet
    - utter_greet
* restaurant_search{"location": "new"}
    - slot{"location": "new"}
    - utter_ask_cuisine
    - export

## Generated Story 1584274112425897363
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": null}
    - utter_ask_email
* email_act{"email": "vipik@gmail.com"}
    - slot{"email": "vipik@gmail.com"}
    - action_SentEmail   
    - utter_email
    - utter_goodbye
    
	
## Generated Story 5929145817448465410
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "Shamli"}
    - utter_Invalid_location
	- slot{"location": "Hyderabad"}
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "Hyderabad"}
    - utter_ask_email
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - action_SentEmail
    - utter_email
    - utter_goodbye
    

## Generated Story 5929145817448465408
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - utter_Invalid_location
	- slot{"location": "delhi"}
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - action_SentEmail
    - utter_email
    - utter_goodbye
   
## Generated Story -2862304723794967271
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
    - utter_Invalid_location
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - action_restaurant
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 4028374026844223931
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "600"}
    - slot{"price": "600"}
    - action_restaurant
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
    - export

## Generated Story 3628873038023539842
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "500"}
    - slot{"price": "500"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
    - export

## Generated Story -5644663428424566902
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "600"}
    - slot{"price": "600"}
    - action_restaurant
    - slot{"location": "kolkata"}
    - utter_ask_email_to_send
* email_act
    - utter_ask_email_address
* email_act
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -2937949914654890946
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": null}
    - utter_Invalid_location
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - slot{"email": "vipinkumar535@gmail.com"}
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -7521505105109964105
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": null}
    - utter_Invalid_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"location": "mexican"}
    - slot{"location": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - action_restaurant
    - slot{"location": "mexican"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* affirm
    - utter_goodbye
    - export

## Generated Story -6918000225978400419
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* goodbye
    - utter_goodbye
    - export

## Generated Story -5065213850383765176
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": null}
    - utter_Invalid_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* affirm
    - utter_ask_email_address
* email_act
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 7291934054388147397
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email_to_send
* email_act
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    - export

