import requests
from datetime import date

PIXELA_API_KEY = "qqwvuiur787AA38646hbchy2863bcyNMTb578237ygbcw"
USERNAME = "mighty-cal"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

pixela_params_create = {
    'token': PIXELA_API_KEY,
    'username': 'mighty-cal',
    'agreeTermsOfService': 'yes',
    'notMInor': 'yes'
}

# pixela_create_response = requests.post(url=pixela_endpoint, json=pixela_params_create)
# pixela_create_response.raise_for_status()
# print(pixela_create_response.text)


# create a graph
graph_params = {
    'id': 'mcgraph1',
    'name': '100 Days Challenge Graph - Python',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

graph_header = {
    'X-USER-TOKEN': PIXELA_API_KEY
}

# create_graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_header)
# create_graph_response.raise_for_status()
# print(create_graph_response.text)


# posting a pixel
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"
yesterdays_date = "20220309"
today_date = date.today().strftime("%Y%m%d")
minutes_done = input("How many minutes did you do today: ")
print(today_date)


post_pixel_params = {
    'date': today_date,
    'quantity': f'{input("How many minutes did you do today: ")}',
}

post_pixel_header = {
    'X-USER-TOKEN': PIXELA_API_KEY
}

# post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=post_pixel_header)
# post_pixel_response.raise_for_status()
# print(post_pixel_response.text)


# update yesterdays data
update_pixel_endpoint = f"{post_pixel_endpoint}/{yesterdays_date}"

update_pixel_params = {
    'quantity': f'{input("How many minutes did you do yesterday? : ")}',
}

update_pixel_header = {
    'X-USER-TOKEN': PIXELA_API_KEY
}
update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=update_pixel_header)
update_pixel_response.raise_for_status()
print(update_pixel_response.text)


# # delete yesterdays data
# delete_pixel_endpoint = f"{post_pixel_endpoint}/{yesterdays_date}"
#
# delete_pixel_header = {
#     'X-USER-TOKEN': PIXELA_API_KEY,
# }
#
# delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=delete_pixel_header)
# delete_pixel_response.raise_for_status()
# print(delete_pixel_response.text)