# Weather Forecast Application Script

class Weather():
    def __init__(self):
        self.weatherdata = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
    }

    def get_weatherdata(self, city):
        return self.get_weatherdata(city, "Weather data not available")

    # Function to provide a detailed weather forecast for a city
    def get_detailed_forecast(city):
        forecast = self.get_weatherdata(city)
        print(f"The weather in {self.get_weatherdata[city]}: {forecast}")

    # Function to parse weather data
    def parse_weather_data(self):
        if not city:
            return "Weather data not available"
        city = self.weatherdata["city"]
        temperature = self.weatherdata["temperature"]
        condition = self.weatherdata["condition"]
        humidity = self.weatherdata["humidity"]
        #self.weatherdata[city] = Weather(city, temperature, condition, humidity)
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# Function to display the basic weather forecast for a city
def display_weather(self):
    data = self.get_weatherdata(city)
    if not data:
        print(f"Weather data not available for {data}")
    else:
        weather_report = self.parse_weather_data(data)
        print(weather_report)

def main():
    weather = Weather()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            weather.get_detailed_forecast(city)
        else:
            weather.display_weather(city)

if __name__ == "__main__":
    main()