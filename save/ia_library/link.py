import requests
import json

# Replace 'YOUR_ITEM_IDS' with a list of item identifiers
item_ids = ['nkshabandmilitary_20170205_0631', 'nordarby_20150801_1958', 'nordarby_20150814_2234']  # Add the desired item IDs here

# Define a dictionary to store item data (ID and download link)
item_data = {}

for item_id in item_ids:
    # Define the API endpoint for retrieving item details
    url = f'https://archive.org/metadata/{item_id}'

    try:
        # Send a GET request to retrieve item details
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Check if the 'downloads' field exists in the item metadata
            if 'downloads' in data:
                # Get the direct download link (URL) for the PDF format
                pdf_download_link = data['downloads']['pdf'][0]['format']['url']

                # Store the item ID and download link in the dictionary
                item_data[item_id] = pdf_download_link
            else:
                item_data[item_id] = "No download links found for this item."
        else:
            item_data[item_id] = f"Error: {response.status_code}"
    except Exception as e:
        item_data[item_id] = f"An error occurred: {e}"

# Save the item data as JSON
output_file_path = 'item_data.json'
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(item_data, json_file, ensure_ascii=False, indent=4)
