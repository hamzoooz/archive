from django.shortcuts import render
import requests
import json
from api.models import ListBook
# Create your views here.

def index(request):
    
    # Initialize an empty list to store item IDs
    item_ids = []

    # Specify the path to the text file containing item IDs
    file_path =  'D:/hamzoooz/files/django/archive.org/archive/api/item_ids.txt'
    # D:\hamzoooz\files\django\archive.org\archive\api\item_ids.txt
# D:\hamzoooz\files\django\archive.org\api\item_ids.txt
    # Open the file and read item IDs line by line
    with open(file_path, 'r') as file:
        for line in file:
            item_id = line.strip()  # Remove leading/trailing whitespace and newline characters
            item_ids.append(item_id)

    # Define a dictionary to store item data (ID and download link)
    item_data = {}

    for item_id in item_ids:
        # Define the API endpoint for retrieving item details
        url = f'https://archive.org/metadata/{item_id}'

        try:
            # Send a GET request to retrieve item details
            response = requests.get(url)

            if response.status_code == 200:
                
                direct_url = requests.get(f'https://archive.org/download/{item_id}/{item_id}.pdf')    
                # Check if the request was successful
                if direct_url.status_code == 200:
                    # Get the current URL from the response object
                    last__link = direct_url.url
                new = ListBook.objects.create(identifier = item_id ,name=item_id,url=f'https://archive.org/download/{item_id}/{item_id}.pdf' , direct_url = last__link)
                
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
        
    listbook = ListBook.objects.all()[0:100]
    
    context = {
        'title' : 'list of books',
        'listbook' : listbook ,
        }
    
    return render(request , "index.html", context)
# ==========================================================

def listbook(request):
    listbook = ListBook.objects.exclude(url=None)
    
    # for i in listbook:
            
    #     response = requests.get(i.url)
    #     if response.status_code == 200:
            # lastlink = response

    context = {
        'title' : 'list of books',
        # 'lastlink' : lastlink,
        'listbook' : listbook ,
        }
    return render(request , "index.html", context)



