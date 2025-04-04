from flask import Flask , render_template, session, sessions, redirect
from flask_app import app # type: ignore
from flask_app.models.user import user # type: ignore
from flask_app.models.recipe import recipe  # type: ignore
from flask import flash


@app.route("/recipes/home")
def recipes_home():
    if "user_id" not in session : 
        flash("You must be logged in to access the dashboard .")
        return redirect ("/")
    
   user = User.get_by_id( sesion["user_id"])

# TO DO 
# Get all the recipes and send to the template
return render_template("home.html", user=user)


# Render Page Details Page One Recipe 
@app.route('/recipes/<recipe_id>')
def recipe_details(recipe_id):
    print ("In details: ", recipe_id)
    # Need to get that recipe from the database
    # Pass recipe into template 
    return render_template('recipe_detail.html')


# Render page with create Form
@app.route('/recipe/new')
def create_page():
    print("In create route .")
    return render_template('create_recipe.html')


# Render Page With Edit Form 
@app.route('/recipe/edit/<recipe_id>')
def edit_page(recipe_id):
    print("In edit page: ", recipe_id)
    # Need to get that recipe from the database
    # Pass recipe into template 
    return render_template('edit_recipe.html')


# GET Action Routes:
#   Delete Route (GET request)
@app.route('/recipe/delete/<recipe_id>')
def delete_recipe(recipe_id):
    print(" In edit page: ", recipe_id)
    #call delete method 
    return redirect('/recipes')


# CREATE ( Process form )
@app.route('/recipes', methodes=['POST'])
def create_recipe():
    print("In the create process Post route:", request.form)
    return redirect('/recipes')



