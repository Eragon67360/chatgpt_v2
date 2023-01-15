"""
VIEWS
"""

import pyrebase

from main import _moduleList
from datetime import datetime

from API import API_FIREBASE
from flet import *

# Your web app's Firebase configuration
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
CONFIG = {
  "apiKey": API_FIREBASE,
  "authDomain": "openai-e318f.firebaseapp.com",
  "projectId": "openai-e318f",
  "storageBucket": "openai-e318f.appspot.com",
  "messagingSenderId": "530087860052",
  "appId": "1:530087860052:web:ddf5bbb0fcd3a62ba7dac1",
  "databaseURL":"https://openai-e318f-default-rtdb.europe-west1.firebasedatabase.app/",
  "measurementId": "G-W6BMTLSTK0"
}


global SESSION
SESSION = {}

firebase = pyrebase.initialize_app(CONFIG)
auth = firebase.auth()
db = firebase.database()


def ChangeRoute(e, page_route):
    global _moduleList

    e.page.views.clear()

    if page_route == '/register':
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_()
        )
        e.page.go("/register")

    if page_route == '/login':
        e.page.views.append(
            _moduleList[page_route].loader.load_module()._view_()
        )
        e.page.go("/login")
        e.page.go("/register")

    else:
        pass

    e.page.update()



# register user when pushing sign up

def Registeruser(e):
    for page in e.page.views[:]:
        if page.route == "/register":
            # Access text fields
            res = e.page.views[0].controls[0].controls[0].content.controls[4] #First name
            try:
                # API to sign new user
                auth.create_user_with_email_and_password(
                    res.controls[2].content.value,
                    res.controls[3].content.value,
                )

                # add user to the database
                data = {
                    "firstName": res.controls[0].content.value,
                    "lastName": res.controls[1].content.value,
                    "email": res.controls[2].content.value,
                }

                for item in res.controls[:]:
                    item.content.value = None
                    item.content.update()

                db.child('users').push(data)
                e.page.views.clear()
                e.page.views.append(_moduleList["/login"].loader.load_module()._view_())

                e.page.update()

            except Exception as e:
                print(e)


def ShowMenu(e):
    
    for page in e.page.views[:]:
        if (page.route != "/login") and (page.route != "/register") and (page.route != None):
            if e.data == 'true':
                page.controls[0].controls[0].controls[0].controls[0].width = 185
                page.update()
            else:
                page.controls[0].controls[0].controls[0].controls[0].width = 60
                page.update()


def LogInUser(e):
    first_name, last_name = GetUserDetails(e)
    print(first_name, last_name)

def GetUserDetails(e):
    global _moduleList
    for page in e.page.views[:]:
        if page.route == '/login':
            res = page.controls[0].controls[0].content.controls[4]

            try:
                user = auth.sign_in_with_email_and_password(
                    res.controls[0].content.value,
                    res.controls[1].content.value,
                )

                SESSION['users'] = user

                val = db.child('users').get()
                for i in val:
                    if i.val()['email'] == user['email']:
                        first_name = i.val()['firstName']
                        last_name = i.val()['lastName']

                        SESSION['path'] = i.key()
                        SESSION['firstName'] = first_name
                        SESSION['lastName'] = last_name

                    return[first_name,last_name]

            
            except  Exception as e:
                print(e)