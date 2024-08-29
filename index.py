from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('formulario.html')


@app.route('/sumar', methods=['POST'])
def sumar():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    suma = num1 + num2
    return f'La suma de {num1} y {num2} es {suma}'
@app.route('/siguiente')

def siguiente():
    return render_template('comparar_numeros.html')



@app.route('/calcular_precio.html', methods=['GET', 'POST'])
def calcular_precios():
    total_pesos = None
    error = None
    if request.method == 'POST':
        try:
            precio1 = float(request.form['precio1'])
            precio2 = float(request.form['precio2'])
            precio3 = float(request.form['precio3'])
            precio4 = float(request.form['precio4'])
            precio5 = float(request.form['precio5'])
            tasa_cambio = float(request.form['tasaCambio'])

            total_dolares = precio1 + precio2 + precio3 + precio4 + precio5
            total_pesos = total_dolares * tasa_cambio
        except ValueError:
            error = "Por favor, ingrese valores numéricos válidos."

    return render_template('calcular_precio.html', total_pesos=total_pesos, error=error)



if __name__ == '__main__':
    app.run(debug=True)
