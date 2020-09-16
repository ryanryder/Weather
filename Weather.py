# THIS IS A CHEAT I AM EDITING CODE I FOUND ONLINE TO GET USED TO API CALLS
# NOT MY CODE!

#Import modules
import requests, json 

#Variables
api_key = "d3fa4ffd35d8326601a390d5c99be957"
url = "http://api.openweathermap.org/data/2.5/weather?"
#city = "Tokyo"
#zip = "03878"
zip = input('Zip Code = ')
units = input('Unit Type = ') #"imperial"

#get API
#complete_url = url + "appid=" + api_key + "&q=" + city
complete_url = url + "appid=" + api_key + "&zip=" + zip + "&units=" + units + ""

# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 

    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
  
    # print following values 
    print(" Temperature (in " + units + " units) = " +
                    str(current_temperature) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ")
