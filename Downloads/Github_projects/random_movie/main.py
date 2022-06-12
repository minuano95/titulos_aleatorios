import os
from random import randint
from requestsTvShow import showsID, get_name
from flask import Flask, render_template, url_for, request, send_from_directory, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

""" 
Moods:
    Pra dormir > Sitcoms
    Feliz/leve > Ação, comédia, aventura, fantasia, mistério 
    Triste > Drama
    Tanto Faz > Sitcoms,Ação, comédia, aventura, fantasia, mistério, Drama
    Animes
"""

app = Flask(__name__)

# class RegistragionForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirmar senha', validators=[DataRequired(), Length(min=6), EqualTo('password')])
#     submit = SubmitField('Se inscrever')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template(r'index.html')

@app.route('/recommendation', methods=["GET", "POST"])
def recommendation():
    series = []
    
    if request.method == 'POST':
        
        if len(request.form.getlist('humor')) == 0:
            return render_template(r'fail.html')
        
        for humor in request.form.getlist('humor'):
            if humor == 'estressado':
                serie_1 = showsID['sitcom'][int(randint(0,len(showsID['sitcom'])-1))]
                serie_2 = showsID['comedy'][int(randint(0,len(showsID['comedy'])-1))]
                for serie in get_name([serie_1, serie_2]):
                    series.append(serie)

            if humor == 'calmo':
                serie_1 = showsID['sitcom'][int(randint(0,len(showsID['sitcom'])-1))]
                serie_2 = showsID['comedy'][int(randint(0,len(showsID['comedy'])-1))]
                serie_3 = showsID['drama'][int(randint(0,len(showsID['drama'])-1))]
                serie_4 = showsID['fantasy'][int(randint(0,len(showsID['fantasy'])-1))]
                for serie in get_name([serie_1, serie_2, serie_3, serie_4]):
                    series.append(serie)
                   
            if humor == 'alegre':
                serie_1 = showsID['sitcom'][int(randint(0,len(showsID['sitcom'])-1))]
                serie_2 = showsID['comedy'][int(randint(0,len(showsID['comedy'])-1))]
                serie_3 = showsID['drama'][int(randint(0,len(showsID['drama'])-1))]
                serie_4 = showsID['science-fiction'][int(randint(0,len(showsID['science-fiction'])-1))]
                serie_5 = showsID['fantasy'][int(randint(0,len(showsID['fantasy'])-1))]
                serie_6 = showsID['action'][int(randint(0,len(showsID['action'])-1))]
                serie_7 = showsID['herois'][int(randint(0,len(showsID['herois'])-1))]
                for serie in get_name([serie_1, serie_2, serie_3, serie_4, serie_5, serie_6, serie_7,]):
                    series.append(serie)
             
            if humor == 'indeciso':
                serie_1 = showsID['sitcom'][int(randint(0,len(showsID['sitcom'])-1))]
                serie_2 = showsID['comedy'][int(randint(0,len(showsID['comedy'])-1))]
                serie_3 = showsID['drama'][int(randint(0,len(showsID['drama'])-1))]
                serie_4 = showsID['science-fiction'][int(randint(0,len(showsID['science-fiction'])-1))]
                serie_5 = showsID['fantasy'][int(randint(0,len(showsID['fantasy'])-1))]
                serie_6 = showsID['action'][int(randint(0,len(showsID['action'])-1))]
                serie_7 = showsID['herois'][int(randint(0,len(showsID['herois'])-1))]
                serie_8 = showsID['animes'][int(randint(0,len(showsID['animes'])-1))]
                for serie in get_name([serie_1, serie_2, serie_3, serie_4, serie_5, serie_6, serie_7, serie_8]):
                    series.append(serie)
                   
            if humor == 'triste':
                serie_1 = showsID['sitcom'][int(randint(0,len(showsID['sitcom'])-1))]
                serie_2 = showsID['action'][int(randint(0,len(showsID['action'])-1))]
                serie_3 = showsID['drama'][int(randint(0,len(showsID['drama'])-1))]        
                for serie in get_name([serie_1, serie_2, serie_3,]):
                    series.append(serie)
                
    series_sortear = []
    for serie in series:
        if serie not in series_sortear:
            series_sortear.append(serie)
    
    print(len(series_sortear))
    show_info = series_sortear[int(randint(a=0, b=len(series_sortear)-1))]
    print(show_info)
    
    return render_template(r'recommendation.html', show_info=show_info)


if __name__ == "__main__":
    app.run()