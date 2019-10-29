from flask import Flask, redirect , request, url_for, render_template
from pymongo import MongoClient
import os
mongo_host = os.environ['MONGOHOST']
client = MongoClient(mongo_host,27017)
db = client.todo
coll = db.mylist

app = Flask(__name__)

@app.route('/update/add',methods=['POST'])
def add():
  work = request.form['task']
  print('request to add task : ',work)                                         #logging info
  flag = False
  for p in coll.find():
    if p['task'] == work:
      flag=True
      break
  if flag:
    print('task already in list!! finish it to add again. \n\n')               #logging info
  else:
    print('adding task : ',work)                                               #logging info
    coll.insert_one({'task':work})
  return redirect(url_for('index'))

@app.route('/update/remove',methods=['POST'])
def remove():
  work = request.form['task']
  print('request to delete task : ',work)                                      #logging info
  flag=False
  for p in coll.find():
    if p['task'] == work:
      flag=True
  if not flag:
    print('task does not exist!! add a task first. \n\n')                      #logging info
  else:
    print('deleting task : ',work)                                             #logging info
    coll.delete_one({'task':work})
  return redirect(url_for('index'))


@app.route('/')
def index():
  print('\n\nconnection [',mongo_host,']\n\n',sep='\0')                        #logging info
  data = []
  for p in coll.find():
     data.append(p)
  print('rendering page now\n')                                                #logging info
  return render_template('index.html',data=data)


if __name__ == "__main__":
        app.run(host="0.0.0.0",debug=True,port="9000")