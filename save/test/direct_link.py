import requests
item_id = "ucl_uwtd12_026"
def get_direct_link(item_id):
    # URL for the Internet Archive API
    api_url = f'https://archive.org/advancedsearch.php'

    # Parameters for the API request
    params = {
        'q': f'identifier:{item_id}',
        'fl': 'identifier',
        'output': 'json'
    }

    # Send GET request to the API
    response = requests.get(api_url, params=params)
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Get the identifier of the item
    identifier = data['response']['docs'][0]['identifier']

    # Direct link to download the item
    direct_link = f'https://archive.org/download/{identifier}/{identifier}.pdf'

    return direct_link

# Replace 'your_item_id' with the ID of the item you want to download
item_id = 'ucl_uwtd12_026'

# Get the direct download link for the item
direct_link = get_direct_link(item_id)
print(direct_link)


