# covid_resource
repo for covid resource tracking

1. Database:
Name, Phone Number, Items, PinCode, City

2. Functionality
 2.1 Anyone can send his/her the item mentioned above to be written in our database
 2.2 Everyone can query based on the postcode or city 

3. Hosting? 
   I don't have much idea about it but lets first complete the project
   
  

create table resources(
  name  varchar, 
  phone varchar primary key, 
  pincode varchar, 
  city varchar, 
  items varchar)
