from flask import Flask, request, render_template
import numpy as np
import  pandas
import sklearn
import pickle

#importing model
model = pickle.load(open('model.pkl', 'rb'))

#creating flask app

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorus'])
    K = int(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['pH'])
    rainfall = float(request.form['Rainfall'])

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1,-1)
    prediction = model.predict(single_pred)

    Crop_dict={0: 'rice', 1: 'papaya', 2: 'watermelon', 3: 'blackgram', 4: 'lentil', 5: 'mango', 6: 'maize', 7: 'chickpea', 8: 'jute',
               9: 'apple', 10: 'coconut', 11: 'muskmelon', 12: 'mothbeans', 13: 'orange', 14: 'pomegranate', 15: 'kidneybeans',
               16: 'banana', 17: 'coffee', 18: 'cotton', 19: 'grapes', 20: 'pigeonpeas', 21: 'mungbean'}

    if predict[0] in Crop_dict:
        crop=Crop_dict[predict[0]]
        result = print('{} is the best crop to be cultivated'.format(crop))
    else:
        result = print('Sorry we are not able to recommend a proper crop for this environment')

    return render_template('index.html',result = result)






# python main
if __name__ == '__main__':
    app.run(debug=True)