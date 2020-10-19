from flask import Flask,request,jsonify,render_template,url_for
import pickle
import numpy as np
app=Flask(__name__)
fire_pickle=pickle.load(open('fire_pickle.pkl','rb'))

@app.route('/')
def home():
    return render_template('onfire.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    ''' A function to measure the 
    predictibility of forest fiore'''
    characters1=[int(y) for y in request.form.values()]
    charac2=[np.array(characters1)]
    #print(characters1)
    #print(charac2)
    probability=fire_pickle.predict_proba(charac2)

    prediction=fire_pickle.predict(charac2)

    probability.astype(int)
    prediction.astype(int)
    print(prediction,type(prediction))
    probabs=round(probability[0][1], 2)
    predicts=prediction[0]
    print(predicts)
    #print(probabs,type(probabs))
    #print(predicts,type(predicts))
    if probabs<=0.5 and predicts==0:
        return render_template('onfire.html',pred_text='Fire will not occur,forest is marked safe and probability of occuring fire is {}'.format(probabs))
    elif probabs>=0.5 and predicts==1:
        return render_template('onfire.html',pred_text='The forest will be on fire Run!! and probability of occuring fire is {}'.format(probabs))
    else:
        return render_template('onfire.html',pred_text='Jangal pe mangal not allowed')


if __name__=='__main__':
    app.run(debug=True)
