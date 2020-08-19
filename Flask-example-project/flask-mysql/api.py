from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields,post_load


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@localhost:3306/flask-mysql'
db = SQLAlchemy(app)

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
        
    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation
    def __repr__(self):
        return '<Author %d>' % self.id

class AuthorsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Authors # definir le model a utiliser pour ce schema
        sqla_session = db.session
    id = fields.Number(dump_only=True) #Mapping de l'attributs id vers un object python
    name = fields.String(required=True)
    specialisation = fields.String(required=True)
    
db.create_all()

#Retourne la liste de tous les autheurs qui figurent dans ma table autheur dans la base de donnée mysql
@app.route('/authors', methods = ['GET'])
def index():
    #SQLALCHEMY recupere la liste de tous les autheurs
    get_authors = Authors.query.all()
    #get_authors = Authors.query.filter(Authors.name == "test").all()
    author_schema = AuthorsSchema(many=True)
    if len(get_authors)>0:
        authors = author_schema.dump(get_authors) #marshmallow serialize tous les objects python autheurs
    else:
        authors = author_schema.dump([])
                         #transformé le resultat en json et    
    return make_response(jsonify({"authors": authors}))

# récupére les données de la requête en JSON, charge les données dans
# le schéma (marshmallow) Authors, puis appele la méthode de création que nous avons créée dans
# la classe Authors qui renverra l'objet créé avec le code d'état 201.
@app.route('/authors', methods = ['POST'])
def create_author():
    data = request.get_json()
    author_schema = AuthorsSchema()
    author = author_schema.load(data)
    result = author_schema.dump(author.create())
    return make_response(jsonify({"author": result}),201)

@app.route('/authors/<id>', methods = ['GET'])
def get_author_by_id(id):
    get_author = Authors.query.get(id)
    author_schema = AuthorsSchema()
    author = author_schema.dump(get_author)
    return make_response(jsonify({"author": author}))

@app.route('/authors/<id>', methods = ['PUT'])
def update_author_by_id(id):
    data = request.get_json()
    get_author = Authors.query.get(id)
    if data.get('specialisation'):
        get_author.specialisation = data['specialisation']
    if data.get('name'):
        get_author.name = data['name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorsSchema(only=['id', 'name','specialisation'])
    author = author_schema.dump(get_author)
    return make_response(jsonify({"author": author}))

@app.route('/authors/<id>', methods = ['DELETE'])
def delete_author_by_id(id):
    get_author = Authors.query.get(id)
    db.session.delete(get_author)
    db.session.commit()
    return make_response("",204)

if __name__ == "__main__":
    app.run(debug=True)