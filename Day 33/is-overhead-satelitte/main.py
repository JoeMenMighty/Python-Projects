import requests
from datetime import datetime
from send_email_from_gmail_ymail import send_from_gmail_ymail
import time

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_in_position():
    status = False
    if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        status = True
    return status


def is_night():
    status = False
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_sunrise = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sunrise.raise_for_status()
    data_sunrise = response_sunrise.json()
    sunrise = int(data_sunrise["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sunrise["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour not in range(sunrise, sunset + 1):
        print("It's dark")
        status = True

    return status


# If the ISS is close to my current position and it's dark
sat_in_position = is_in_position()
is_night_time = is_night()
while True:
    time.sleep(60)
    if sat_in_position:
        msg = f"Subject: Satellite status \n\nCurrent position is latitude: {iss_latitude} " \
              f"longitude: {iss_longitude} and satellite is close"
        if is_night_time:
            msg += f"\n It's Dark as well, Look Up !!!"
    else:
        msg = f"Subject: Satellite status \n\nBoring stuff happening !!!"
    print(msg)
    send_from_gmail_ymail(msg, "myglomail1@gmail.com")
