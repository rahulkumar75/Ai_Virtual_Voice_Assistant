import requests

def search_advice(query, num_advice):
    # API endpoint URL for searching advice
    url = f'https://api.adviceslip.com/advice/search/{query}'

    try:
        # ***********************************todo Random Advice
        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            advice_data = response.json()

            # todo search advice
            advice_slips = advice_data['slips']
            # Extract advice text from each advice slip and print
            count = 0

            for slip in advice_slips:
                if count < num_advice:
                    advice = slip['advice']
                    print('Advice:', advice)
                    count = count + 1
                else:
                    break
        else:
            print(f"Error: Unable to fetch advice. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Example usage
# random_advice = get_random_advice()
# if random_advice:
#     print("Random Advice:", random_advice)

# Example usage: Search for advice containing the word "love"
# search_advice('money', 3)
