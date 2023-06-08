from flask import Flask, render_template, request,jsonify
import json
from waitress import serve

from pymongo import MongoClient

app = Flask(__name__)

# Sample data for dropdown options
dropdown_options = ['Option 1', 'Option 2', 'Option 3']




# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['Chirag']  # Replace 'your_database' with your actual database name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search']
        # Perform search logic here
        
        # Render template with search results
        return render_template('index.html', search_term=search_term)
    else:
        return render_template('index.html', dropdown_options=dropdown_options)


@app.route('/Search/<data>', methods=['GET', 'POST'])
def Search(data):
    
    mycol = db["chirag"]
    # mycol.create_index([('Sticker No', 'text')])
    
    results = mycol.find({'$text': {'$search': data}},{"_id":0}).limit(3)
    

    # mylist=[]
    # for i in results:
    #     mylist.append(i)
    
    # print(mylist)
    # serialized_list = [str(item) for item in mylist]
    


    
       
    json_data = json.dumps(list(results), default=str)
    print(json_data)
    
    return json_data


@app.route('/Research', methods=['GET', 'POST'])
def R_Search(data):
       

    
    data=["some random data ","date","id","vehilce_no","Vehicle_Name"]
    return ["asd","Asd","As"]
   

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)