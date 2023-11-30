from api.app import db

class Questionario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
      
    pinterna1 = db.Column(db.String) #Pergunta
    qinterna1 = db.Column(db.String)
    pinterna2 = db.Column(db.String) #Pergunta
    qinterna2 = db.Column(db.String)
    pinterna3 = db.Column(db.String) #Pergunta
    qinterna3 = db.Column(db.String)
    pinterna4 = db.Column(db.String) #Pergunta
    qinterna4 = db.Column(db.String)
    pinterna5 = db.Column(db.String) #Pergunta
    qinterna5 = db.Column(db.String)
    pinterna6 = db.Column(db.String) #Pergunta
    qinterna6 = db.Column(db.String)
    pinterna7 = db.Column(db.String) #Pergunta
    qinterna7 = db.Column(db.String)
    pinterna8 = db.Column(db.String) #Pergunta
    qinterna8 = db.Column(db.String)

class QuestionarioExterno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
      
    pexterna1 = db.Column(db.String) #Pergunta
    qexterna1 = db.Column(db.String)
    pexterna2 = db.Column(db.String) #Pergunta
    qexterna2 = db.Column(db.String)
    pexterna3 = db.Column(db.String) #Pergunta
    qexterna3 = db.Column(db.String)
    pexterna4 = db.Column(db.String) #Pergunta
    qexterna4 = db.Column(db.String)
    pexterna5 = db.Column(db.String) #Pergunta
    qexterna5 = db.Column(db.String)
    pexterna6 = db.Column(db.String) #Pergunta
    qexterna6 = db.Column(db.String)
    pexterna7 = db.Column(db.String) #Pergunta
    qexterna7 = db.Column(db.String)
    pexterna8 = db.Column(db.String) #Pergunta
    qexterna8 = db.Column(db.String)