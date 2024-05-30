#2. Refactoring a Weather Forecast Application into Classes and Modules
#Task 2:Identifying and Creating Classes

# Weather Forecast Application Script

class Weather:
    def __init__(self):
        # Simulated data based on city
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        
    def get_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.get_weather_data(city, {})

    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = self.get_weather_data(city, {})
        return parse_weather_data(data)
    
    def display_weather(city):
        # Function to display the basic weather forecast for a city
        data = self.get_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = parse_weather_data(data)
            print(weather_report)

    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"




