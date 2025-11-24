"""
API: Aplicacion programing interface
Nasa API:https://api.nasa.gov/
API_KEY_NASA: YOUR NASA API_KEY
developer : jhon carlos bastidas vallejo
date 09/11/2025
script  description: get and read data from NASA API aboout cometsand others 
https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}  

"""
import requests
import os

os.system("cls")

def get_nasa_data(api_key):

    print("::: comet information :::")

    # Construir URL de NASA sin espacios
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"

    # Realizar la solicitud a la API
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print(data)


API_KEY_NASA = "eLn9UjMSYSWcLHQIzsM6OH3zwqP5gWIf7nDs9b9w"
get_nasa_data(API_KEY_NASA)
