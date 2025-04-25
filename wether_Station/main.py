import requests
import json

while input("Press Enter to continue and q to quit: ")!="q":
    city=input("Please Enter Your City Name: ")
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1ed6219a920e748e463f58c5b81c79ed"
    #above one is a formated string for city 
    data=requests.get(url)
    if data.status_code==200: # checks if the data is fetched properly or not
        data=json.loads(data.text) #converts the string data into DICTIONARY format
        print(f"🏙️ City Name: {data['name']}")
        print(f"🌡️ City Temperature: {data['main']['temp']} °C")
        print(f"🥶 City Feels like: {data['main']['feels_like']}°C")
        print(f"💦 City Humidity: {data['main']['humidity']}%")
        print(f"🌇 City Sky: {data['weather'][0]['description']}")
        print(f"🍃 City Wind: {data['wind']['speed']}km/hr")
        

    else:
        print("Could Not find Place")
