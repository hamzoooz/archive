# configration the ia
from internetarchive import configure
configure('bookhope.com@gmail.com', 'Hamza@2020')

from internetarchive import get_files
fnames  = get_files(identifier='2_20201027' )



all_item_ids = []

# with open('arabic_ids.txt', 'a') as file:
