# It's a project for fun don't you nag me

# - How to Test :)
##  first make a config.json file in the root of the project
## in config.json
```
{
    SECRET_KEY": "secret",
    "EMAIL_HOST_USER": "<YOUR-GMAIL-ADDRESS>@gmail.com",
    "EMAIL_HOST_PASSWORD": "<YOUR-GMAIL-PASSWORD>",
}
```
### also make sure you have third party apps allowed in your gmail account
# -------------------------------------------
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 3 manage.py migrate
$ python3 3 manage.py runserver 
```
# ------------------------------------------
# TODO
- user password reset
- user's email have to be valid 
- make this ugly pages look nice :/


