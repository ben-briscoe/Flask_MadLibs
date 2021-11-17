from flask import Flask, request, render_template, redirect, flash
from functions import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Uncool01!"



@app.route('/madlib-form')
def show_form():
    return render_template('madlib_form.html')



@app.route('/your-story')
def make_story():
    place = request.args.get('place')
    noun = request.args.get('noun')
    verb = request.args.get('verb')
    adjective = request.args.get('adjective')
    pnoun = request.args.get('pnoun')
    input = [place,noun,verb,adjective,pnoun]
    print(input)
    not_filled_out = make_sure_its_filled_out(input)
    if not_filled_out:
        flash('Please Make Sure All Fields Are Filled Out')
        return redirect('/madlib-form')
        
    return render_template('your_story.html', place=place, noun=noun, verb=verb,adjective=adjective, pnoun=pnoun)

