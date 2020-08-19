from main import afficher
from direbonjour import somme,coeficient
from flask import Flask

app=Flask(__name__)

@app.route('/sommes/<a>/<b>')
def url_somme(a,b):    
    return str(int(a)*int(b)*int(coeficient))

if __name__=="__main__":
    app.run()

    