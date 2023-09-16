# configration the ia
from internetarchive import configure
configure('bookhope.com@gmail.com', 'Hamza@2020')

# to download item by id or item collections etc...
from internetarchive import download
# download('ucl_uwtd1217_004', verbose=True , formats="pdf" , ignore_existing=True , on_the_fly=True )
download('2_20201027', verbose=True  )


# Email address: bookhope.com@gmail.com
# Password:  Hamza@2020



