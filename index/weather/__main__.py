from weather import weather_generator

def main():
    city = input("Enter the city name: ")
    celsius_temperature, fahrenheit_temperature, condition = weather_generator.generate_weather()
    print(f"Current Temperature in {city}: {celsius_temperature}°C/{fahrenheit_temperature}°F")
    print(f"Weather Condition: {condition}")

if __name__ == "__main__":
    main()