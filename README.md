# Registration2Calendar

##Information
This project is for **Bogazici University** students only.

Once complete, users will be able to see the classes they attend to in their calendars.

##Usage

Currently id numbers and passwords are hardcoded in the single python code.

```
my_user_id="YOUR_USER_ID"
my_user_pass="YOUR_USER_PASSWORD"

```

In the near future a better io interface will be provided for this purpose.

###Features
* Implemented
  1. Provided that the credentials are correct, fetch the registration  web page
  2. Parse this web page, create a well-structured dataset containing relevant data on the schedule
* NOT Implemented
  1. Using Google calendar API, create a new calendar
  2. Populate the calendar with the data provided from registration
