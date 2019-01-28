## Generated Story -277470545592324679
* goodbye
    - utter_goodbye
	
## Generated Story -277470545592325679
* goodbye
    - utter_goodbye
	
## Generated Story -277470545592327679
* goodbye
    - utter_goodbye
	
## Generated Story -277470545592328679
* goodbye
    - utter_goodbye
	
## Generated Story -277470545592329679
* goodbye
    - utter_goodbye
	
## Generated Story -277470545592323679
* goodbye
    - utter_goodbye
	
## Generated Story -277470145592323679
* deny
    - utter_no_email_sent
	
## Generated Story -277470245592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
	
## Generated Story -277470345592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
	
## Generated Story -277470445592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
	
## Generated Story -277470645592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
	
## Generated Story -277470745592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
	
## Generated Story -277470845592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
	
## Generated Story -277470945592323679
* deny
    - utter_no_email_sent
	- utter_goodbye
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
	
## Generated Story 1732454364351689134
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "399"}
    - slot{"price": "399"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* affirm
    - utter_ask_email_address
* email_act{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_SentEmail
    - utter_email_sent
	- utter_goodbye	
	
## Generated Story 1584274112425897363
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validate_location
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
    - utter_ask_email_to_send
* email_act{"email": "vipik@gmail.com"}
    - slot{"email": "vipik@gmail.com"}
    - action_SentEmail   
    - utter_email_sent    
    - utter_goodbye
	
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
## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* email_act{"email": "vipik@gmail.com"}
    - slot{"email": "vipik@gmail.com"}
    - action_SentEmail   
    - utter_email_sent    
    - utter_goodbye
	
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
* email_act{"email": "vipik@gmail.com"}
	- slot{"email": "vipik@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    
	
## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- utter_Invalid_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
      - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* email_act{"email": "vipik@gmail.com"}
    - slot{"email": "vipik@gmail.com"}
    - action_SentEmail   
    - utter_email_sent    
    - utter_goodbye

## Generated Story 5929145817448465410
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "Shamli"}    
	- action_validate_location
	- slot{"location": ""}
	- utter_Invalid_location
	- slot{"location": "Hyderabad"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "Hyderabad"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - utter_email_sent    
    - utter_goodbye

## Generated Story 5929145817448465408
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
	- action_validate_location
	- slot{"location": ""}
    - utter_Invalid_location
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - utter_email_sent    
    - utter_goodbye

## Generated Story 5929145817448465418
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
	- action_validate_location
	- slot{"location": ""}
    - utter_Invalid_location
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - utter_email_sent    
    - utter_goodbye
	
## Generated Story 5929145817448465408
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
	- action_validate_location
	- slot{"location": ""}
    - utter_Invalid_location
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - utter_email_sent    
    - utter_goodbye

## Generated Story 5929145817448465418
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
	- action_validate_location
	- slot{"location": ""}
    - utter_Invalid_location
	- slot{"location": "delhi"}
	- action_validate_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar@gmail.com"}
    - slot{"email": "vipinkumar@gmail.com"}
    - action_SentEmail
    - utter_email_sent    
    - utter_goodbye
	
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
	
## Generated Story -2862304723794967271
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "sharanpur"}
    - slot{"location": "sharanpur"}
    - action_validate_location
    - slot{"location": null}
    - utter_Invalid_location
	- slot{"location": "rishikesh"}
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
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye

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
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    
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
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye

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
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye
    
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
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - utter_email_sent
    - utter_goodbye

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
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
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
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
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
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "701"}
    - slot{"price": "701"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* affirm
    - utter_goodbye

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
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": "800"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* affirm
    - utter_goodbye
	
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
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": "800"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* affirm
    - utter_goodbye
	
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
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": "800"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* affirm
    - utter_goodbye
	
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
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": "800"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
* affirm
    - utter_goodbye
	
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
	
## Generated Story -6918000225978400419
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "350"}
    - slot{"price": "350"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
	
## Generated Story -6918000225978400419
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "250"}
    - slot{"price": "250"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
	
## Generated Story -6918000225978400419
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - action_validate_location
    - slot{"location": "bengaluru"}
    - utter_ask_price
* restaurant_search{"price": "250"}
    - slot{"price": "250"}
    - action_restaurant
    - slot{"location": "bengaluru"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
	
## Generated Story -6918000225978400419
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - action_validate_location
    - slot{"location": "bengaluru"}
    - utter_ask_price
* restaurant_search{"price": "250"}
    - slot{"price": "250"}
    - action_restaurant
    - slot{"location": "bengaluru"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent
	
## Generated Story -6918000225978400419
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "bengaluru"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bengaluru"}
    - action_validate_location
    - slot{"location": "bengaluru"}
    - utter_ask_price
* restaurant_search{"price": "250"}
    - slot{"price": "250"}
    - action_restaurant
    - slot{"location": "bengaluru"}
    - utter_ask_email_to_send
* deny
    - utter_no_email_sent

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
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - slot{"email": "vipinkumar535@gmail.com"}    
    - utter_email_sent
    - utter_goodbye
	
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
* restaurant_search{"price": "500"}
    - slot{"price": "500"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - slot{"email": "vipinkumar535@gmail.com"}    
    - utter_email_sent
    - utter_goodbye

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
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - slot{"email": "vipinkumar535@gmail.com"}    
    - utter_email_sent
    - utter_goodbye
	
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
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email_to_send
* email_act{"email": "vipinkumar535@gmail.com"}
    - slot{"email": "vipinkumar535@gmail.com"}
    - action_SentEmail
    - slot{"email": "vipinkumar535@gmail.com"}    
    - utter_email_sent
    - utter_goodbye