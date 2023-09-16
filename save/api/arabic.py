import requests
import json

# Define the API endpoint for the Internet Archive's search API
url = 'https://archive.org/advancedsearch.php'

# Define the search query to filter by the "books by language Arabic" collection
search_query = 'collection:booksbylanguage_arabic'

# Specify additional search parameters
params = {
    'q': search_query,
    'fl[]': 'identifier,title',  # Retrieve the identifier and title fields
    'rows': 500,  # Number of results per page (adjust as needed)
    'page': 1,  # Initial page number
    'output': 'json',  # Output format
}

# Initialize a list to store item data (ID and title)
all_items = []

while True:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        docs = data.get('response', {}).get('docs', [])
        
        if not docs:
            break  # No more items to retrieve
        
        for item in docs:
            item_data = {
                'id': item['identifier'],
                'title': item['title'][0] if 'title' in item else None,
            }
            all_items.append(item_data)

        # Increment the page number for the next request
        params['page'] += 1
    else:
        print(f"Error: {response.status_code}")
        break

# Save the retrieved item data as JSON
output_file_path = 'item_data.json'
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_items, json_file, ensure_ascii=False, indent=4)

print(f"Item data saved to {output_file_path}")






# import requests

# # Define the API endpoint for the Internet Archive's search API
# url = 'https://archive.org/advancedsearch.php'

# # Define the search query to filter by the "books by language Arabic" collection
# search_query = 'collection:booksbylanguage_arabic'

# # Specify additional search parameters
# params = {
#     'q': search_query,
#     'fl[]': 'identifier',  # Retrieve only the identifier field (the item ID)
#     'rows': 500,  # Number of results per page (adjust as needed)
#     'page': 1,  # Initial page number
#     'output': 'json',  # Output format
# }

# # Initialize a list to store the item IDs
# all_item_ids = []

# while True:
#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         docs = data.get('response', {}).get('docs', [])
#         item_ids = [item['identifier'] for item in docs]

#         if not item_ids:
#             break  # No more items to retrieve

#         all_item_ids.extend(item_ids)

#         # Increment the page number for the next request
#         params['page'] += 1
#     else:
#         print(f"Error: {response.status_code}")
#         break

# # Print the retrieved item IDs
# for item_id in all_item_ids:
#     print(item_id)

# # You can also save the item IDs to a file if needed
# with open('arabic_ids.txt', 'w') as file:
#     for item_id in all_item_ids:
#         file.write(f"{item_id}\n")
