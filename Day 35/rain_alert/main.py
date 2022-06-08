import requests
from twilio.rest import Client


# latitude and longitude for Accra
MY_LAT = 5.603717
MY_LONG = -0.186964
TWILIO_ACCOUNT_SID = "ACdac96ba682b9a88e632348bd07006ee1"
TWILIO_AUTH_TOKEN = "0a79b68fc415edebc5c57429f0f1b776"

# my api key
api_key1 = "e13dc0bb1b4ec607dcaaef15266b47f9"
api_key2 = "d4682971990e3ad4204e2d1742307f93"

# api url
api_url = "https://api.openweathermap.org/data/2.5/onecall"

# make call to open weather api
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key1,
    "exclude": "current,minutely,daily"
}


response = requests.get(url=api_url, params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data_sliced = response.json()["hourly"][: 11]

weather_codes = [hour_data["weather"][0]["id"] for hour_data in weather_data_sliced]

will_rain = False

msg = "All is safe... Feel free to go to work"

for val in weather_codes:
    if int(val) < 700:
        msg = "It's likely to rain today, Carry your Umbrella !!!"
        will_rain = True
        break

# send sms using twillio
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body=msg,
    from_='+17163034273',
    to='+233501588573'
)

print(message.status)
