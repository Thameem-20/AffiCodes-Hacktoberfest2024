import requests

# Function to get weather data
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Constructing complete URL
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    # Sending request
    response = requests.get(complete_url)
    
    # Parsing JSON response
    data = response.json()
    
    # Check if the city is found
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        # Extracting data
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]
        
        # Output the weather details
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")
    else:
        print("City not found! Please enter a valid city name.")

# Main function to take user input
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace this with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    get_weather(city, api_key)
