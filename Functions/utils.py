import pytz
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import json
import discord
import random
## Get current IST date ##

def current_ist_date():
    tz = pytz.timezone('Asia/Kolkata')
    date = datetime.now(tz).date()
    return(date.strftime('%d/%m/%Y'))

## Get date after X month(s) from todays date ##

def date_after_X_months_and_Y_days(months: int, days=0):
    tz = pytz.timezone('Asia/Kolkata')
    date = datetime.now(tz).date()
    date_after_X_months_and_Y_days1 = date + relativedelta(months=months)
    if days != 0:
        date_after_X_months_and_Y_days1 = date_after_X_months_and_Y_days1 + timedelta(days=14)
    return(date_after_X_months_and_Y_days1.strftime('%d/%m/%Y'))

## check the date is bigger or not ##

def is_date_old(date):
    d, m, y = date.split("/")
    date1 = datetime(int(y), int(m), int(d))

    d1, m1, y1 = current_ist_date().split("/")
    date2 = datetime(int(y1), int(m1), int(d1))
    return(date1>date2)

## Check if the buyers sub is expired or not (Takes buyers user_id as input and Returns True if buyers sub end date is valid) ##

def is_buyer_valid(user_id: str):
    buyers_data = []
    file = open('Database/buyers_data.json', 'r')
    buyers_data = json.load(file)
    file.close()
    buyer_found = []
    for i in range(len(buyers_data)):
        if buyers_data[i]["user_id"] == user_id:
            buyer_found.append(i)
            if buyers_data[i]["user_data"]["sub_type"] == "Lifetime":
                return("VALID")
            else:
                date = buyers_data[i]["user_data"]["sub_end"]
                d, m, y = date.split("/")
                date1 = datetime(int(y), int(m), int(d))

                d1, m1, y1 = current_ist_date().split("/")
                date2 = datetime(int(y1), int(m1), int(d1))
                if date1>date2:
                    return("VALID")
                else:
                    return("EXPIRED")
    if len(buyer_found) == 0:
        return("NOT A BUYER")

## filtre troops name ##

def filtre_troop_name(string):
    string = string.strip().lower()
    string = string.replace(' ', '')
    string = string.replace('.','')
    return string

## generate google play rece code ##

def getno():
	y = f"{random.randint(0, 9)}"
	h = f"{random.randint(0, 9)}"
	j = f"{random.randint(0, 9)}"
	k = f"{random.randint(0, 9)}"
	to = y + h + j + k
	return (to)

## get a discord user object ##

def get_user(user_id:discord.User):
    user = user_id
    return (user)