from flask import Flask,request,render_template
import pickle

modelo = pickle.load(open('modelo2.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html',titulo="Previsão")

@app.route('/predicaoform',methods=['POST'])
def form():
    if len(request.form['area']) != 0:
        area = float(request.form['area'].replace(",", "."))
    else:
        area = 0 

    if len(request.form['perimeter']) != 0:
        perimeter = float(request.form['perimeter'].replace(",", "."))
    else:
        perimeter = 0 
    
    if len(request.form['major-axis']) != 0:
        majorAxis = float(request.form['major-axis'].replace(",", "."))
    else:
        majorAxis = 0 

    if len(request.form['minor-axis']) != 0:
        minorAxis = float(request.form['minor-axis'].replace(",", "."))
    else:
        minorAxis = 0 
    
    if len(request.form['aspect-ration']) != 0:
        aspectRation = float(request.form['aspect-ration'].replace(",", "."))
    else:
        aspectRation = 0 

    if len(request.form['eccentricity']) != 0:
        eccentricity = float(request.form['eccentricity'].replace(",", "."))
    else:
        eccentricity = 0 
   
    if len(request.form['convex-area']) != 0:
        convexArea = float(request.form['convex-area'].replace(",", "."))
    else:
        convexArea = 0 
    
    if len(request.form['equiv-diameter']) != 0:
        equivDiameter = float(request.form['equiv-diameter'].replace(",", "."))
    else:
        equivDiameter = 0 
    
    if len(request.form['extent']) != 0:
        extent = float(request.form['extent'].replace(",", "."))
    else:
        extent = 0 
    
    if len(request.form['solidity']) != 0:
        solidity = float(request.form['solidity'].replace(",", "."))
    else:
        solidity = 0 
    
    if len(request.form['roundness']) != 0:
        roundness = float(request.form['roundness'].replace(",", "."))
    else:
        roundness = 0 
    
    if len(request.form['compactness']) != 0:
        compactness = float(request.form['compactness'].replace(",", "."))
    else:
        compactness = 0 
    
    if len(request.form['shape-factor-1']) != 0:
        shapeFactorOne = float(request.form['shape-factor-1'].replace(",", "."))
    else:
        shapeFactorOne = 0 
    
    if len(request.form['shape-factor-2']) != 0:
        shapeFactorTwo = float(request.form['shape-factor-2'].replace(",", "."))
    else:
        shapeFactorTwo = 0 
  
    if len(request.form['shape-factor-3']) != 0:
        shapeFactorThree = float(request.form['shape-factor-3'].replace(",", "."))
    else:
        shapeFactorThree = 0 
    
    if len(request.form['shape-factor-4']) != 0:
        shapeFactorFour = float(request.form['shape-factor-4'].replace(",", "."))
    else:
        shapeFactorFour = 0 

    resultado = modelo.predict([[area,perimeter,majorAxis,minorAxis,aspectRation,eccentricity,convexArea,equivDiameter,extent,solidity,roundness,compactness,shapeFactorOne,shapeFactorTwo,shapeFactorThree,shapeFactorFour]])
    return render_template('resultado.html',titulo="Previsão", resultado=resultado)


app.run(debug=True)