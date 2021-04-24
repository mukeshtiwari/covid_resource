from flask import Flask
app = Flask(__name__)


#this function takes picode and 
#returns the list of suppliers
@app.route('/pincode/<string:pcode>')
def fetch_data_by_pincode(pcode):
  return 'Pincode is %s' % pcode

#this function takes city and 
#returns the list of suppliers
@app.route('/city/<string:name>')
def fetch_data_by_city(name):
  return 'city is %s' % name

@app.route('/hello/<name>')
def hello_world(name):
  return 'Hello %s' % name 

if __name__ == '__main__':
   app.run()