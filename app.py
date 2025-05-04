from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

agora = datetime.now().year

def validarData(data):
    if data > agora:
        raise Exception("Insira uma data válida")
    return data
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    try:
        data = validarData(int(request.form.get('data')))
        resultado = (agora - data)
        print(resultado)
        return render_template('index.html', resultado=f'{resultado} ano{'s' if resultado != 1 else ''} de idade')
    except Exception as e:
        return render_template('index.html', erro=f'Insira uma data válida')

if __name__ == '__main__':
    app.run()