#Flask, Streamlit, Gradio, Django
import pickle
from flask import Flask,request,render_template

app=Flask(__name__)
model=pickle.load(open('salary.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    tecrube=float(request.form.get('tecrube'))
    yazili=float(request.form.get('yazili'))
    mulakat=float(request.form.get('mulakat'))
    tahmin=float(model.predict([[tecrube,yazili,mulakat]]))
    tahmin=round(tahmin,2)
    return render_template('index.html',
                           tahmin='Yapay Zekâ Modeli tarafından tahmin edilen gelir\n ${}'.format(tahmin))
if __name__=='__main__':
    app.run(debug=True)
