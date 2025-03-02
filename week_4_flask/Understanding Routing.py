from flask import Flask, abort

app = Flask(__name__)

# Route racine qui répond avec "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World!"

# Route /dojo qui répond avec "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Route /say/<name> qui répond avec "Hi" suivi du nom dans l'URL
@app.route('/say/<name>')
def say_hi(name):
    # Vérifie si le nom est une chaîne de caractères
    if not name.isalpha():
        abort(400, description="Le nom doit être une chaîne de caractères.")
    return f"Hi {name.capitalize()}!"

# Route /repeat/<int:num>/<word> qui répète le mot autant de fois que spécifié
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    # Vérifie si le numéro est un entier et si le mot est une chaîne de caractères
    if not isinstance(num, int) or not word.isalpha():
        abort(400, description="Le nombre doit être un entier et le mot doit être une chaîne de caractères.")
    return (word + " ") * num

# Gestion des erreurs pour les routes non définies
@app.errorhandler(404)
def not_found(error):
    return "Désolé ! Aucune réponse. Essayez à nouveau.", 404

if __name__ == "__main__":
    app.run(debug=True)