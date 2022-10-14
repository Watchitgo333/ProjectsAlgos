from flask import Flask, render_template, session, redirect, request, flash
from FlaskApp import app
from FlaskApp.Models.User import User

@app.route ("/")
def Index ():
    return render_template ("login_reg.html")

@app.route ("/register", methods = ["POST"])
def Register ():
    valid_user = User.create_valid_user (request.form)
    print(request.form)
    if not valid_user:
        print(valid_user)
        return redirect ("/")
        # return redirect ("/Register")
    session ["userID"] = valid_user.id
    return redirect ("/home")

@app.route ("/login", methods = ["POST"])
def Login ():
    valid_user = User.authenticated_user_by_input (request.form)
    if not valid_user:
        return redirect ("/")
    session ["userID"] = valid_user.id
    return redirect ("/home")

@app.route ("/logout")
def Logout ():
    session.clear ()
    return redirect ("/")