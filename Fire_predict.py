from flask import Flask,request,jsonify,render_template,url_for
import pickle
import numpy as np
app=Flask(__name__)
fire_pickle=pickle.load(open('fire_pickle.pkl','rb'))

@app.route("/")
def home():
    return render_template('onfire.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    characters1=[int(y) for y in request.form.values()]
    charac2=[np.array(characters1)]
    print(characters1)
    print(charac2)
    prediction=fire_pickle.predict_proba(charac2)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output==0.00:
        return render_template('onfire.html',pred_text='Fire will not occur,forest is marked safe')
    elif output==1.00:
        return render_template('onfire.html',pred_text='The forest will be on fire,Run!!')
    else:
        return render_template('onfire.html',pred_text='Jangal pe mangal not allowed')


if __name__=='__main__':
    app.run(debug=True)
