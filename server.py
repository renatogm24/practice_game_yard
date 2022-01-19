from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hola_mundo():
  return 'Hola Mundo!'

@app.route('/play')
def play():
  return render_template("index.html", number=3)

@app.route('/play/<int:number>')
def playNum(number):
  return render_template("index.html", number=number, color = "blue")

@app.route('/play/<int:number>/<string:color>')
def playNumColor(number, color):
  return render_template("index.html", number=number, color = color)

# @app.route('/say/<string:name>')
# def say(name):
#   return f"¡Hola, {name}!"

# @app.route('/repeat/<int:num>/<string:word>')
# def repeat(num,word):
#   return render_template('index.html')
# 	return render_template("index.html", phrase="hola", times=5)

# @app.route('/<word>/')
# def anything(word):
#   if word not in ["dojo","say","repeat"]:
#     return "¡Lo siento! No hay respuesta. Inténtalo otra vez."

if __name__=="__main__":
  app.run(debug=True)