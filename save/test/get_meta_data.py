# import PyPDF2

# # Replace 'your_pdf_file.pdf' with the path to your PDF file
# # pdf_file_path = 'https://archive.org/download/ucl_uwtd12_026/ucl_uwtd12_026.pdf'
# pdf_file_path = 'https://ia804506.us.archive.org/11/items/ucl_uwtd12_026/ucl_uwtd12_026.pdf'

# # Open the PDF file in read-binary mode
# with open(pdf_file_path, 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)

#     # Get the number of pages in the PDF
#     num_pages = pdf_reader.numPages

#     # Get document information (metadata)
#     document_info = pdf_reader.getDocumentInfo()

#     # Extract metadata attributes
#     author = document_info.author
#     creator = document_info.creator
#     producer = document_info.producer
#     subject = document_info.subject
#     title = document_info.title
#     keywords = document_info.keywords
#     creation_date = document_info.created
#     modification_date = document_info.modified

# # Print the extracted metadata
# print(f"Author: {author}")
# print(f"Creator: {creator}")
# print(f"Producer: {producer}")
# print(f"Subject: {subject}")
# print(f"Title: {title}")
# print(f"Keywords: {keywords}")
# print(f"Creation Date: {creation_date}")
# print(f"Modification Date: {modification_date}")


import requests
import PyPDF2
from io import BytesIO

# Replace 'your_pdf_url' with the URL of your PDF file
# pdf_url = 'https://ia804506.us.archive.org/11/items/ucl_uwtd12_026/ucl_uwtd12_026.pdf'
pdf_url = 'https://archive.org/download/ucl_uwtd12_026/ucl_uwtd12_026.pdf'

# Download the PDF file
response = requests.get(pdf_url)
response.raise_for_status()

# Open the downloaded PDF file in memory as a byte stream
pdf_file = PyPDF2.PdfReader(BytesIO(response.content))
# pdf_file = PyPDF2.PdfReader(response.content)

# Get the number of pages in the PDF
# num_pages = pdf_file.numPages
num_pages = len(pdf_file.pages)

# Get document information (metadata)
# document_info = pdf_file.getDocumentInfo()
document_info = pdf_file.metadata

# Extract metadata attributes
author = document_info.author
creator = document_info.creator
producer = document_info.producer
subject = document_info.subject
title = document_info.title
# keywords = document_info.keywords
# creation_date = document_info.created
# modification_date = document_info.modified

# Print the extracted metadata
print(f"Author: {author}")
print(f"Creator: {creator}")
print(f"Producer: {producer}")
print(f"Subject: {subject}")
print(f"Title: {title}")
# print(f"Keywords: {keywords}")
# print(f"Creation Date: {creation_date}")
# print(f"Modification Date: {modification_date}")

