from flask import Flask, render_template, request,jsonify
import json
from waitress import serve

from pymongo import MongoClient

app = Flask(__name__)






# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['Chirag']  # Replace 'your_database' with your actual database name


@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello"


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



   

if __name__ == '__main__':
    app.run()