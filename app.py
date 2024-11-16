from flask import Flask, request, render_template

from Anlyze_data import analyze_data

from generate_graphs import generate_graphs
app = Flask(__name__)


@app.route('/')
def home():
    survival_rate, class_distribution = analyze_data()
    generate_graphs()
    return render_template(
        "index.html",
        survival_rate=survival_rate,
        class_distribution=class_distribution
    )

@app.route('/welcome')
def Bienvenidos():
    return 'Hola Bienvenidos a mi pagina web!'
@app.route('/user/<name>/<int:age>')
def get_user(name, age):
    return f"Hola {name}! tu edad es {age} años"

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Bienvenido, {name}"
    return"""
        <form method="post">
            Nombre: <input type="text" name="name"
            <input type="submit">
        </form>
    """




if __name__ == '__main__':
    app.run()
