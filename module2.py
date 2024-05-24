from module1 import Weather

def main():
    city_weather = Weather()
    while True:
        try:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                city_weather.get_detailed_forecast(city)
            else:
                city_weather.display_weather(city)
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    main()