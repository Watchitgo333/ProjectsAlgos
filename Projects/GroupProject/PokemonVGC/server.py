from FlaskApp.Control import Users, Pokemons
from FlaskApp import app


if __name__ == "__main__":
    app.run ("localhost", port=5000, debug = True)