from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask import render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljjr1989jjlyyaf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'


db = SQLAlchemy(app)
csrf = CSRFProtect(app)

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

class QuestionForm(FlaskForm):
    nome = StringField("Digite seu nome:", validators=[InputRequired()])
    
    #Interna
    #Manutenibilidade
    pinterna1 = StringField("Em uma escala de 1 a 10, qual é a facilidade percebida para fazer atualizações no sistema?", validators=[InputRequired()])
    qinterna1 = TextAreaField("", validators=[InputRequired()])
    pinterna2 = StringField("Os desenvolvedores consideram que o código-fonte é bem estruturado e fácil de entender?",validators=[InputRequired()])
    qinterna2 = TextAreaField( validators=[InputRequired()])
    #Conformidade:
    pinterna3 = StringField("Quantas normas de código limpo e padrões financeiros reconhecidos são aplicados pelo sistema?",validators=[InputRequired()])
    qinterna3 = TextAreaField( validators=[InputRequired()])
    pinterna4 = StringField("Há feedback positivo dos colaboradores da empresa sobre a conformidade do sistema?",validators=[InputRequired()])
    qinterna4 = TextAreaField( validators=[InputRequired()])
    #Eficiência:
    pinterna5 = StringField("Qual é o tempo médio de processamento para concluir um registro no sistema?", validators=[InputRequired()])
    qinterna5 = TextAreaField( validators=[InputRequired()])
    pinterna6 = StringField("Os usuários relatam alguma lentidão ou problemas de desempenho durante o uso do sistema?", validators=[InputRequired()])
    qinterna6 = TextAreaField( validators=[InputRequired()])
    #Confiabilidade:
    pinterna7 = StringField("Qual a porcentagem de precisão nas informações geradas pelo sistema?",validators=[InputRequired()])
    qinterna7 = TextAreaField( validators=[InputRequired()])
    pinterna8 = StringField("Os usuários confiam nas informações fornecidas pelo sistema para tomar decisões?",validators=[InputRequired()])
    qinterna8 = TextAreaField( validators=[InputRequired()])


class QuestionExternoForm(FlaskForm):
    nome = StringField("Digite seu nome:", validators=[InputRequired()])
    
    #Externo
    #Funcionalidade
    pexterna1 = StringField("", validators=[InputRequired()])
    qexterna1 = TextAreaField("", validators=[InputRequired()])
    pexterna2 = StringField("",validators=[InputRequired()])
    qexterna2 = TextAreaField( validators=[InputRequired()])
    #Confiabilidade
    pexterna3 = StringField("",validators=[InputRequired()])
    qexterna3 = TextAreaField( validators=[InputRequired()])
    pexterna4 = StringField("",validators=[InputRequired()])
    qexterna4 = TextAreaField( validators=[InputRequired()])
    #Usabilidade
    pexterna5 = StringField("",validators=[InputRequired()])
    qexterna5 = TextAreaField( validators=[InputRequired()])
    pexterna6 = StringField("",validators=[InputRequired()])
    qexterna6 = TextAreaField( validators=[InputRequired()])
    #Eficiência de Desempenho
    pexterna7 = StringField("",validators=[InputRequired()])
    qexterna7 = TextAreaField( validators=[InputRequired()])
    pexterna8 = StringField("",validators=[InputRequired()])
    qexterna8 = TextAreaField( validators=[InputRequired()])


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    questionarios = Questionario.query.all()
    questionariosExternos = QuestionarioExterno.query.all()
    return render_template('index.html', questionarios=questionarios, questionariosExternos=questionariosExternos)

# DETALHE FORMULARIO INTERNO
@app.route('/formulario/<int:id>')
def formulario_detalhes(id):
    questionario = Questionario.query.get(id)
    return render_template('formulario_detalhes.html', questionario=questionario)

# DETALHE FORMULARIO EXTERNO
@app.route('/form_externo/<int:id>')
def form_externo_detalhes(id):
    questionarioExterno = QuestionarioExterno.query.get(id)
    return render_template('form_externo_detalhes.html', questionarioExterno=questionarioExterno)


#ADICIONAR FORMULARIO
@app.route('/add_formulario', methods=['GET', 'POST'])
def add_formulario():
    form = QuestionForm()
    if form.validate_on_submit():
        questionario = Questionario(nome=form.nome.data, 
                                    pinterna1=form.pinterna1.data,  #Pergunta   
                                    qinterna1=form.qinterna1.data,  
                                    pinterna2=form.pinterna2.data,  #Pergunta     
                                    qinterna2=form.qinterna2.data,
                                    pinterna3=form.pinterna3.data,  #Pergunta
                                    qinterna3=form.qinterna3.data, 
                                    pinterna4=form.pinterna4.data,  #Pergunta
                                    qinterna4=form.qinterna4.data, 
                                    pinterna5=form.pinterna5.data,  #Pergunta
                                    qinterna5=form.qinterna5.data,
                                    pinterna6=form.pinterna6.data,  #Pergunta
                                    qinterna6=form.qinterna6.data,
                                    pinterna7=form.pinterna7.data,  #Pergunta
                                    qinterna7=form.qinterna7.data,
                                    pinterna8=form.pinterna8.data,  #Pergunta
                                    qinterna8=form.qinterna8.data,)
        db.session.add(questionario)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_formulario.html', form=form)


@app.route('/add_form_externo', methods=['GET', 'POST'])
def add_form_externo():
    form = QuestionExternoForm()
    if form.validate_on_submit():
        questionarioExterno = QuestionarioExterno(nome=form.nome.data, 
                                    pexterna1=form.pexterna1.data,  #Pergunta   
                                    qexterna1=form.qexterna1.data,  
                                    pexterna2=form.pexterna2.data,  #Pergunta     
                                    qexterna2=form.qexterna2.data,
                                    pexterna3=form.pexterna3.data,  #Pergunta
                                    qexterna3=form.qexterna3.data, 
                                    pexterna4=form.pexterna4.data,  #Pergunta
                                    qexterna4=form.qexterna4.data, 
                                    pexterna5=form.pexterna5.data,  #Pergunta
                                    qexterna5=form.qexterna5.data,
                                    pexterna6=form.pexterna6.data,  #Pergunta
                                    qexterna6=form.qexterna6.data,
                                    pexterna7=form.pexterna7.data,  #Pergunta
                                    qexterna7=form.qexterna7.data,
                                    pexterna8=form.pexterna8.data,  #Pergunta
                                    qexterna8=form.qexterna8.data,)
        db.session.add(questionarioExterno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_form_externo.html', form=form)


#EDITAR
@app.route('/edit_formulario/<int:id>', methods=['GET', 'POST'])
def edit_formulario(id):
    questionario = Questionario.query.get(id)
    form = QuestionForm(obj=questionario)

    if form.validate_on_submit():
        form.populate_obj(questionario)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_formulario.html', form=form, questionario=questionario)


@app.route('/edit_form_externo/<int:id>', methods=['GET', 'POST'])
def edit_form_externo(id):
    questionarioExterno = QuestionarioExterno.query.get(id)
    form = QuestionExternoForm(obj=questionarioExterno)

    if form.validate_on_submit():
        form.populate_obj(questionarioExterno)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_form_externo.html', form=form, questionarioExterno=questionarioExterno)


#DELETAR
@app.route('/delete_formulario/<int:id>', methods=['GET', 'POST'])
def delete_formulario(id):   
    questionario = Questionario.query.get(id)
    db.session.delete(questionario)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_form_externo/<int:id>', methods=['GET', 'POST'])
def delete_form_externo(id):   
    questionarioExterno = QuestionarioExterno.query.get(id)
    db.session.delete(questionarioExterno)
    db.session.commit()
    return redirect(url_for('index'))
   




if __name__ == '__main__':
   
    app.run(debug=True)

