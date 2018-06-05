from flask import Flask, render_template, request,jsonify,json,url_for,redirect
from forms import ContactForm,LoginForm
from forms  import LoginForm
from forms import UpdateForm
from wtforms import ValidationError
import os
app = Flask(__name__)
app.config['SECRET_KEY']='13381aff9ceea1d02dbf8995d5c539a3'
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   if request.method == 'POST':
      if form.validate() == False:
         return render_template('contact.html', form = form)
      else:
            d={}
            value1=request.form['fname']
            value2=request.form['lname']
            value3=request.form['age']
            value4=request.form['mobileno']
            value5=request.form['email']
            value6=request.form['password']
            d['Firstname']=value1
            d['Lastname']=value2
            d['Age']=value3
            d['Mobileno']=value4
            d['Email']=value5
            d['Password']=value6
            data=json.dumps(d,indent=4,sort_keys=True)
            with open('json_file.json', 'a') as f1:
                if os.stat("json_file.json").st_size==0:
                    f1.write("[")
                    f1.write("\n")
                    f1.write("\t")
                    f1.write(data)
                    f1.write("]")
                else:
                    with open('json_file.json','rb+') as f1:
                        f1.seek(-1,os.SEEK_END)
                        f1.truncate()
                    with open('json_file.json','a') as f1:
                        f1.write("\n")
                        f1.write("\t")
                        f1.write(",")
                        f1.write(data)
                        f1.write("]")
            return redirect(url_for('success')) 
   elif request.method == 'GET':
         return render_template('contact.html', form = form)
@app.route('/SignIn', methods = ['GET', 'POST'])
def SignIn():
    form =LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('LoginForm.html', form = form)
        else:
            Firstname_value=request.form['Firstname']
            password_value=request.form['password']
            with open("json_file.json","r") as f:
                    data = f.read() 
                    value1=str(Firstname_value)
                    value2=str(password_value)
                    d = json.loads(data)
                    for i in d :
                       if i['Firstname'] ==value1 and i['Password']==value2:
                         return redirect(url_for('success'))
                    
                       else:
                           continue
                    return redirect(url_for('failure'))
    elif request.method == 'GET':
         return render_template('LoginForm.html', form = form)

@app.route('/success', methods = ['GET', 'POST'])
def success(): 
        return render_template('success.html')
@app.route('/failure', methods = ['GET', 'POST'])
def failure(): 
    return render_template('failure.html')
         
@app.route('/update', methods = ['GET','POST'])
def update():  
    form =UpdateForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('update.html', form = form)
        else:
            value1=request.form['fname']
            value2=request.form['lname']
            value3=request.form['age']
            value4=request.form['mobileno']
            value5=request.form['email']
            value6=request.form['password']
            with open("json_file.json","r") as f:
                    data = f.read() 
                    d = json.loads(data)
                    value=str(value5)
                    i = [i for i in d if i['Email'] == value]
                    i[0]['Firstname']=value1
                    i[0]['Lastname']=value2
                    i[0]['Mobileno']=value4
                    i[0]['Age']=value3  
                    i[0]['Email']=value5
                    i[0]['Password']=value6                                  
                    info=json.dumps(d,indent=4,sort_keys=True)
                    with open("json_file.json",'w') as file1:
                        file1.write(info)  
                    return "successfully updated" 
    elif request.method == 'GET':
            return render_template('update.html', form = form)
if __name__ == '__main__':
   app.run(debug = True)  