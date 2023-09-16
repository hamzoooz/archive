import requests
# from bs4 import BeautifulSoup

# Define the URL
item_id = "gu_deafmutesjo19300724"

# Define the URL
url = f'https://archive.org/download/{item_id}/{item_id}.pdf'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the current URL from the response object
    current_url = response.url
    
    # Print or use the current URL as needed
    print("Current URL:", current_url)
else:
    print("Failed to retrieve the page.")

# You can now use the 'current_url' variable for further processing or store it as needed.
