import requests
from datetime import datetime
import time

MY_LAT = -35.280937
MY_LNG = 149.130005

def isIssOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_lat = float(data["iss_position"] ["latitude"])
    iss_lng = float(data["iss_position"] ["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lng <= MY_LNG+5:
        return True

def isNight():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:
    
    if isIssOverhead() and isNight():
        print("Look Up👆\n\nThe ISS is above you in the sky.")
    elif isIssOverhead == True and isNight == False:
        print("The ISS is overhead but its not night so you cannot see :(")
    else:
        print("The ISS is not overhead")
    time.sleep(60)