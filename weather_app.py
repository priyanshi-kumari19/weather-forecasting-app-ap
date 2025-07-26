import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your actual API key
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\n📍 City: {data['name']}, {data['sys']['country']}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"🌥️ Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s\n")
    else:
        print(f"❌ Error: {data.get('message', 'City not found or API issue')}")

# Run it
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
