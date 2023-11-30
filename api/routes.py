from flask import render_template, redirect, url_for
from api import app, db
from api.models import Questionario, QuestionarioExterno
from api.form import QuestionForm, QuestionExternoForm


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
