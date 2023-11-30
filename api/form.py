from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

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
