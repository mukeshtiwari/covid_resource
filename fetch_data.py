
#this function takes picode and 
#returns the list of suppliers
def fetch_data_by_pincode(pincode):
  #here we will connect to database
  #and query it.
  f = open("/Users/mukesht/Mukesh/Github/covid_resource/resource_item.text")

  ret = []
  for x in f:
    t = x.split(',')
    if ((t[2].strip()) == pincode.strip()):
      ret.append(x)

  return ret 


#this function takes city and 
#returns the list of suppliers
def fetch_data_by_city(city):
  #here we will connect to database
  #and query it.
  f = open("/Users/mukesht/Mukesh/Github/covid_resource/resource_item.text")

  ret = []
  for x in f:
    t = x.split(',')
    if ((t[3].strip().lower()) == city.strip().lower()):
      ret.append(x)

  return ret 

print(fetch_data_by_pincode('234567'))
print(fetch_data_by_city('Varanasi'))
