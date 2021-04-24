
#this function would write data in the database
def write_data(name, phone, pincode, city, resources):
  #here we will connect to database
  #and write to it
  f = open('/Users/mukesht/Mukesh/Github/covid_resource/resource_item.text', 'a')
  f.write(name + ', ' + phone + ', ' + pincode + ', ' + city + ', [' + resources + ']\n')
  f.close()


write_data("Hello World", "657254762", "232101", "Mughalsarai", "[ Oxygen, Vaccine ]")