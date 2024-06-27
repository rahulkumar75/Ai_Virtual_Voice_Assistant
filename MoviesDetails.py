from Speak import Say
import requests
import credential


def moviesInfo():
    # Replace 'YOUR_API_KEY' with your actual OMDb API key
    api_key = credential.movie_api_key

    # Base URL for OMDb API
    base_url = 'http://www.omdbapi.com/'

    # Movie title to search for
    Say('Enter Movie Name:')
    movie_title = input()

    # Construct the API request URL
    url = f'{base_url}?apikey={api_key}&t={movie_title}'

    # Send GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        movie_data = response.json()

        # Display movie information
        print('Title:', movie_data['Title'])
        print('Year:', movie_data['Year'])
        print('Rated:', movie_data['Rated'])
        print('Released:', movie_data['Released'])
        print('Runtime:', movie_data['Runtime'])
        print('Genre:', movie_data['Genre'])
        print('Director:', movie_data['Director'])
        print('Writer:', movie_data['Writer'])
        print('Actors:', movie_data['Actors'])

        print('Language:', movie_data['Language'])
        print('Country:', movie_data['Country'])
        print('Awards:', movie_data['Awards'])
        print('Poster URL:', movie_data['Poster'])
        print('IMDb Rating:', movie_data['imdbRating'])  # Display IMDb rating
        print('Plot:', movie_data['Plot'])
    else:
        print('Error:', response.status_code)

        # You can access more information from the 'movie_data' dictionary
        # Access more information from the 'movie_data' dictionary
