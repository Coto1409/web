from flask import Flask
import random

app = Flask(__name__)

DT = [
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

@app.route("/")
def index():
    return '''
        <h1>Hola, acá puedes aprender un poco sobre dependencias tecnológicas</h1>
        <a href="/random_fact">¡Ver un dato aleatorio!</a><br>
        <a href="/caraosello">Jugar cara o sello</a>
    '''

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(DT)}</p><br><a href="/">Volver</a>'

@app.route("/caraosello")
def caraosello():
    resultado = random.choice(["Cara", "Sello"])
    return f'''
        <h2>Resultado: {resultado}</h2>
        <form action="/caraosello">
            <button type="submit">Lanzar de nuevo</button>
        </form>
        <br>
        <a href="/">Volver</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)
