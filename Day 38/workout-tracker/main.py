import requests
from datetime import datetime

APP_ID = "5c852868"
API_KEY = "422f0444d274e1dfe7ad163c7f839ed3"
GENDER = "male"
WEIGHT_KG = 78.3
HEIGHT_CM = 198.40
AGE = 24

nlp_nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nlp_params = {
 "query": input("What exercise did you do today?: "),
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE
}

nlp_headers = {
 'x-app-id': APP_ID,
 'x-app-key': API_KEY
}


nlp_response = requests.post(url=nlp_nutrition_endpoint, json=nlp_params, headers=nlp_headers)
nlp_response.raise_for_status()
nlp_info = nlp_response.json()['exercises'][0]
# print(nlp_response.text)


## getting data from sheety and posting to sheety
sheety_endpoint = "https://api.sheety.co/38992ecbc793bcad3a069267f1eadb31/myWorkouts/workouts/"

#
new_excersise_entry = {
 'workout': {
  'date': str(datetime.now().date().strftime("%d/%m/%Y")),
  'time': datetime.now().time().strftime("%H:%M:%S"),
  'exercise': nlp_info['name'].title(),
  'duration': nlp_info['duration_min'],
  'calories': nlp_info['nf_calories'],
  }
}


sheety_response = requests.post(url=sheety_endpoint, json=new_excersise_entry)
# sheety_response.raise_for_status()
print(sheety_response.text)

