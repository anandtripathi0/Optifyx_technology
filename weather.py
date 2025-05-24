import requests
api_key="dd7cdcebec1e2ad887d916201cfbfdda"
base_url="http://api.openweathermap.org/data/2.5/weather?"

city_name=input("Enter your city name OR ZIP CODE : ")
complete_url=base_url+"appid="+api_key+"&q="+city_name

response=requests.get(complete_url)
x=response.json()
if x["cod"] != "404":
    y=x["main"]
    current_temperature=y["temp"]
    current_pressure=y["pressure"]
    current_humidity=y["humidity"]
    z=x["weather"]
    weather_description=z[0]["description"]
    print(" Temperature = " + str(f"{current_temperature-273.15:.2f}°C") + "\n Atmospheric pressure = " + str(f"{current_pressure}hPa") + "\n Humidity = " + str(f"{current_humidity}%") + "\n Description = " + str(weather_description))
else:
    print("error")    
