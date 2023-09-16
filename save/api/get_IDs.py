import requests
import time

# Define the API endpoint for advanced search
# url = 'https://archive.org/advancedsearch.php'
url = 'https://archive.org/details/booksbylanguage_arabic'

# Define your search query for texts
# search_query = 'collection:texts AND mediatype:texts'
search_query = 'collection:texts AND mediatype:texts'

# Specify additional search parameters
params = {
    'q': search_query,
    'fl[]': 'identifier',  # Retrieve only the identifier field (the item ID)
    'rows': 500,  # Number of results per page (adjust as needed)
    'page': 1,  # Initial page number
    'output': 'json',  # Output format
}

# Initialize a list to store the item IDs
all_item_ids = []

while True:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        docs = data.get('response', {}).get('docs', [])
        item_ids = [item['identifier'] for item in docs]

        if not item_ids:
            break  # No more items to retrieve

        all_item_ids.extend(item_ids)

        # Increment the page number for the next request
        params['page'] += 1

        # Add a delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust the delay as needed
    else:
        print(f"Error: {response.status_code}")
        break

# # Print the retrieved item IDs
# for item_id in all_item_ids:
#     print(item_id)

    # You can also save the item IDs to a file if needed
    with open('arabic_ids.txt', 'a') as file:
        for item_id in all_item_ids:
            file.write(f"{item_id}\n")









 