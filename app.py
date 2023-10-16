# Import libraries
import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle
app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)
    return render_template('index.html', output='Predicted salary :{}'.format(prediction))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)