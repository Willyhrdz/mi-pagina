from flask import Flask

app = Flask(__name__)

mi_pagina = '''
<html>
<body>
<h1>Hola novia!</h1>
<h2>Te amo</h2>
<img src='https://www.birthdaywishes.expert/wp-content/uploads/2018/12/feliz-navidad-imagen-papa-noel.jpg'>
</body>
</html>
'''

@app.route('/')
def hola_mundo():
   return mi_pagina

@app.route('/<name>')
def hola_nombre(name):
   return 'Hola %s!' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)