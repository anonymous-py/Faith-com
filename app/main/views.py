from . import main
from flask import render_template, redirect, url_for, request, redirect, flash


@main.route('/')
def home():
    if request == "POST":
        function = request.form['random']

        if function:
            flash("testing the function with flask", 'success')
        else:
            flash("na bruv , it doest work")
    return render_template('home.html')
