from flask import Flask , request , render_template , jsonify
import pymongo 
import pandas as pd
app = Flask(__name__)


import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route('/',methods=['GET','POST'])
def hello_world():
    return render_template('Index.html')
    
@app.route("/data",methods=['POST'])
def func():
    if request.method =='POST':
        file=request.form['upload-file']
        open_file=pd.read_excel(file)
        return render_template('data.html',data=open_file.to_html())

@app.route('/connection_string')
def my_form():
    return render_template('connection_string.html')

@app.route("/db1",methods=['POST'])

def db1():
        text = request.form['text']
        client = pymongo.MongoClient(text)
        db = client['k_db']
        d= db['k']
        for x in d.find():
            return JSONEncoder().encode(x)
        return render_template('db1.html')
@app.route('/connection_string_db2')
def string_db2():
    return render_template('connection_string_db2.html')
@app.route('/db2',methods=['POST'])
def db2():
    if request.method=='POST':
        db2 = request.form['text']
        
        return render_template('db2.html',data=db2)
if __name__== '__main__':
    app.run(debug=True)
    