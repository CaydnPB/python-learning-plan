import random

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9//5) + 32
    return fahrenheit

def generate_weather():
    celsius_temperature = random.randint(0, 50)
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Thunderstorm']
    condition = random.choice(weather_conditions)
    return celsius_temperature, fahrenheit_temperature, condition