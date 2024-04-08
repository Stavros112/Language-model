import requests
import json


def get_weather(city):
    api_key = 'd00ef812239a5796b15a7a13ed01e0c7'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        for i in range(3):
            forecast_time = data['list'][8*i]['dt_txt']
            forecast_weather = data['list'][8*i]['weather'][0]['description']
            forecast_temp = data['list'][8*i]['main']['temp']
            print(f"At {forecast_time}, the weather in {city} will be {forecast_weather} with a temperature of {forecast_temp}°C.")
    else: 
        print('Sorry, I could not find what you are looking for. Please try again')

def recommend_restaurant(location, cuisine_style):
    api_key = 'bSUAGz9B_4AHYUYWJAVW7hXEJK9SDGH7cYPbXdSWRK6FzrI68keOzDRh6zc1CWABDfv4Q7Nf2AKKKYRYlOAVlVTZiSxrgd1kUzPaqDYoGo0iCUNa9dp9tkXkap0AZHYx'
    # Set up the Yelp Fusion API endpoint and parameters
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer ' + api_key}
    params = {'location': location, 'term': cuisine_style, 'sort_by': 'rating', 'limit': 1}

    # Send a GET request to the Yelp Fusion API endpoint
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and extract the recommended restaurant name and address
        data = json.loads(response.text)
        restaurant_name = data['businesses'][0]['name']
        restaurant_address = data['businesses'][0]['location']['address1']

        # Return the recommended restaurant name and address
        return f"Recommended restaurant: {restaurant_name}\nAddress: {restaurant_address}"
    else:
        # If the request was not successful
        print('Sorry, I could not find what you are looking for. Please try again')


def chatbot():

    keywords_weather = ['weather', 'Weather', 'raining', 'Raining', 'snowing', 'Snowing', 'clouds', 
    'Clouds', 'cloudy', 'Cloudy', 'rainy', 'Rainy', 'rain', 'Rain', 'snow', 'Snow', 'fog','Fog', 'foggy',
    'Temperature', 'temperature', 'Humidity', 'humidity', 'Wind', 'wind', 'windy', 'Storm', 'storm', 'Thunderstorm', 
    'Sunny', 'sunny', 'Sun', 'sun']
    
    keywords_food = ['restaurant', 'eat', 'dinner', 'lunch', 'food', 'eating', 'dining', 'Restaurant', 
    'Eat', 'Dinner', 'Lunch', 'Food', 'Eating', 'Dining', 'drink', 'drinking', 'bar', 'cocktail']

    keywords_exit = ['exit', 'bye', 'goodbye', 'Exit', 'Bye', 'Goodbye', 'Thank you', 'thanks', 
    'thank you', 'Thanks', 'thank', 'Thank' ]

    while True:
        input_text = input("Hi! How can I help you?\n")
        if any([x in input_text for x in keywords_weather]):
            print(input_text)
            city = input("For which city would you like to know the weather?\n")
            print(city)
            print(get_weather(city))
        elif any([x in input_text for x in keywords_food]):
            print(input_text)
            location = input("Where are you looking for a restaurant?\n")
            print(location)
            cuisine_style = input("What type of cuisine are you in the mood for?\n")
            print(cuisine_style)
            print(recommend_restaurant(location, cuisine_style))
        elif any([x in input_text for x in keywords_exit]):
            print(input_text)
            print('Goodbye')
            break
        else:
            print("Sorry, I don't understand. Please try again.")

chatbot()