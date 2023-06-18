from flask import Flask, render_template, request,jsonify
import json
from waitress import serve
from flask_cors import CORS

import pymongo

app = Flask(__name__)



CORS(app)


# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://ChiragRohada:s54icYoW4045LhAW@atlascluster.t7vxr4g.mongodb.net/test")
db = client['vehicle']  # Replace 'your_database' with your actual database name


@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello"


@app.route('/lo', methods=['GET', 'POST'])
def lo():
    return {"hello":"hello"}


@app.route('/search/<data>', methods=['GET', 'POST'])
def Search(data):
    
    mycol = db["c"]
    # mycol.create_index([('Vehicle No', 'text')])
    
    results = mycol.find({'$text': {'$search': data}},{"_id":0}).limit(5)
    

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