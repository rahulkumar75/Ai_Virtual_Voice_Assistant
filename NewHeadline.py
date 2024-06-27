import requests
import credential


# Function to get the latest news
def get_latest_news():

    api_key = credential.news_api_key
    country = 'in'  # print('You can specify a country code')
    category = None  # print('Optional: specify a news category')
    query = None  # print('Optional: specify a query to search for in headlines')

    # Base URL for News API
    base_url = "https://newsapi.org/v2/top-headlines"

    # Define query parameters
    params = {
        'apiKey': api_key,
        'country': country,  # You can specify a country code, e.g., 'us' for the United States
        'category': category,  # Optional: specify a news category, e.g., 'technology', 'sports', etc.
        'q': query  # Optional: specify a query to search for in headlines
    }

    # Make the HTTP GET request to the News API
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        # Check if there are articles in the response
        if articles:
            print("Latest News:")
            # Display the top headlines (you can limit the number as needed)
            for i, article in enumerate(articles[:5], start=1):
                title = article['title']
                source = article['source']['name']
                print(f"{i}. {title} ({source})")
        else:
            print("No news articles found.")
    else:
        print(f"Failed to retrieve news. Status code: {response.status_code}")




# get_latest_news(api_key, country, category, query)  # Fetch the latest news headlines from the United States



# Categories:
# News API supports the following categories:

# business: News related to business and finance.
# entertainment: News related to the entertainment industry.
# general: General news that doesn't fall under any specific category.
# health: News related to health and medicine.
# science: News related to scientific discoveries and research.
# sports: News related to sports events and activities.
# technology: News related to technology and IT industry.
# politics: News related to politics (not an official category, but you can use query to filter news).
# You can specify the category in the parameters of your function when fetching news articles.

# Query:
# The query parameter allows you to search for specific topics in news articles. For example, you can search for news articles containing terms such as:
#
# Python: To search for news related to the Python programming language.
# election: To search for news related to elections.
# COVID-19: To search for news related to the COVID-19 pandemic.
# SpaceX: To search for news about the SpaceX company and its space missions.
# climate change: To search for news about climate change.
# You can specify a query in the parameters of your function when fetching news articles. The function will then return news articles that contain the specified query in their titles or descriptions.
