from flask import Flask, render_template, session, redirect, request
from FlaskApp import app
from FlaskApp.Models.User import User
from flask import flash

@app.route ("/home")
def Home ():
    if "userID" not in session:
        flash ("You must be logged in to access this dashboard")
        return redirect ("/")
    user = User.get_by_ID (session ["userID"])
    return render_template ("home.html", user = user)

@app.route ("/top_cut")
def Trainer ():
    if "userID" not in session:
        flash ("You must be logged in to access this dashboard")
        return redirect ("/")
    user = User.get_by_ID (session ["userID"])
    users = User.get_all ()
    print (user)
    return render_template ("top_cut.html", users=users)

@app.route ("/teams")
def Usage ():
    if "userID" not in session:
        flash ("You must be logged in to access this dashboard")
        return redirect ("/")
    user = User.get_by_ID (session ["userID"])
    teams = User.get_all ()
    return render_template ("teams.html", teams=teams)
    valid

@app.route ("/edit/<int:id>", methods = ["GET", "POST"])
def Edit (id):
    if 'userID' not in session:
        return redirect ("/")
    if request.method == "GET":
        user = User.get_by_ID (session ["userID"])
        print(user)
        return render_template ("edit.html", user = user)
    if request.method == "POST":
        user = User.get_by_ID (session ["userID"])
        trainer = request.form
        valid_trainer = User.editTeam (trainer, session ["userID"])
        if not valid_trainer:
            return redirect (f"/edit/{id}")
        trainer = User.get_by_ID (id)
        return redirect (f"/teams")

@app.route ("/team_builder", methods = ["GET", "POST"])
def New ():
    # response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
    # print(response)
    # print(json.dumps(response.json()))
    if 'userID' not in session:
        return redirect ("/")
    if request.method == "GET":
        user = User.get_by_ID (session ["userID"])
        return render_template ("team_builder.html", user = user)
    elif request.method == "POST":
        user = User.get_by_ID (session ["userID"])
        print (request.form)
        valid_trainer, trainer_id = User.createTeam (request.form, user = user)
        if valid_trainer:
            trainer = User.get_by_ID (trainer_id)
            return redirect (f"/teams")
        if not valid_trainer:
            flash("Please choose a Pokemon from each list provided", "pokemon")
            return redirect(f"/team_builder")

@app.route ("/delete/<int:id>")
def Delete (id):
    if 'userID' not in session:
        return redirect ("/")
    user = User.get_by_ID (id) 
    User.delete_user_by_id (id)
    return redirect (f"/teams")