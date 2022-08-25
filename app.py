from threading import local
from unittest import result
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('savedmodel1.sav','rb'))

@app.route('/')
def hello():
    result=''
    # if request.method=='POST':
    #     print('post')
    #     score1=request.form.get('score1')
    #     score2=request.form.get('score2')
    #     failure=request.form.get('failure')
    #     sex=request.form.get('sex')
    #     return render_template ("index.html",result=[score1,score2])
    return render_template("index.html",**locals())


@app.route('/predict',methods=['POST','GET'])
def predict():
    score1=float(request.form.get('score1'))
    score2=float(request.form.get('score2'))
    failure=float(request.form.get('failure'))
    sex=float(request.form.get('sex'))
    fedu=float(request.form.get('fedu'))
    medu=float(request.form.get('medu'))
    fjob=request.form.get('fjob')
    mjob=request.form.get('mjob')
    if (fjob=='Teacher'):
         ar1=[0,0,0,0,1]
    elif (fjob=='Medical'):
        ar1=[0,1,0,0,0]
    elif (fjob=='Services'):
        ar1=[0,0,0,1,0]
    elif (fjob=='Home'):
        ar1=[1,0,0,0,0]
    elif (fjob=='Other'):
        ar1=[0,0,1,0,0]

    if (mjob=='Teacher'):
         ar2=[0,0,0,0,1]
    elif (mjob=='Medical'):
        ar2=[0,1,0,0,0]
    elif (mjob=='Services'):
        ar2=[0,0,0,1,0]
    elif (mjob=='Home'):
        ar2=[1,0,0,0,0]
    elif (mjob=='Other'):
        ar2=[0,0,1,0,0]

    result = model.predict([[failure,sex,medu,fedu,score1,score2,ar2[0],ar2[1],ar2[2],ar2[3],ar2[4],ar1[0],ar1[1],ar1[2],ar1[3],ar1[4]]])[0]
    pred=round(float(result),2)

    # result = model.predict([[failure,sex,medu,fedu,score1,score2,0,0,0,0,0,0,0,0,0,0]])[0]
    # pred=int(result)

    return render_template ("index.html",pred=pred)

if __name__ == "__main__":
    app.run(debug=True)
