from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''<html>
        <header>
            <title>Mon super site</title>        
        </header>
        <body>
            <h1 style="width:300px;margin:0 auto;">Hello tout le monde</h1>
            <table style="width:100%;color:red">
                <thead>
                    <tr>
                        <td>column1</td>
                        <td>column2</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>je suis column1</td>
                        <td>je suis column2</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>'''

@app.route('/test')
def test():
    return 'test'

@app.route('/autheur')
def auheur():
    return '<h1>je suis auteur</h1>'

@app.route('/calcul/<nombre>')
def fois10(nombre):    
    return str(int(nombre)*10)

@app.route('/jemultipli/<a>/multiplication/<b>/<c>')
def multiplication(a,b,c):    
    return str(int(a)*int(b)*int(c))
    

if __name__== '__main__':
    app.run()