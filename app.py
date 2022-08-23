from threading import local
from unittest import result
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('savedmodel.sav','rb'))

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
    score1=int(request.form.get('score1'))
    score2=int(request.form.get('score2'))
    failure=int(request.form.get('failure'))
    sex=int(request.form.get('sex'))
    fedu=int(request.form.get('fedu'))
    #fjob=int(request.form.get('fjob'))
    medu=int(request.form.get('medu'))
    #mjob=int(request.form.get('mjob'))
    result = model.predict([[failure,sex,medu,fedu,score1,score2,0,0,0,0,0,0,0,0,0,0]])[0]
    pred=int(result)

    return render_template ("index.html",pred=pred)

if __name__ == "__main__":
    app.run(debug=True)
