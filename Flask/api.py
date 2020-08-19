from flask import Flask, request

app = Flask(__name__) #Initialisation de l'application

@app.route('/') #lié ce endpoint (url) à la fonction hello_world
def test():
    return hello_world()

@app.route('/coucou')
def coucou():
    return 'coucou'

@app.route('/somme/<a>/plus/<b>')
def somme(a,b):
    somme=int(a)+int(b)
    return str(somme)

@app.route('/multiplication/<a>/<b>')
def multi(a,b):
    m=int(a)*int(b)
    return str(m)


listeFitec=[]

           #url  + une methode http = endpoints 
@app.route('/fitec',methods=['GET'])
def fitecGET():    
    return str(listeFitec)

            #url  + une methode http = endpoints
@app.route('/fitec',methods=['POST'])
def fitecPOST():    
    
    # requete http reçu request         
    
    #recuperation du json encapsulé dans la requette http
    data=request.get_json()    

    listedeslivres=data["books"]

    for livre in listedeslivres:
        print("=========================")
        print("Titre : "+livre["titre"])
        print("resumé : "+livre["resume"])
        print("=========================")
    
    return "je suis entrain de tester"

@app.route('/afficher')
def afficher():
    return '''
        <html>
            <head>
                <title></title>
            </head>
            <body>
                <h1>je suis une page d'un site web</h1>
            </body>
        </html>
    '''

# cette partie doit toujours etre à la fin du script
if __name__== '__main__':
    app.run()