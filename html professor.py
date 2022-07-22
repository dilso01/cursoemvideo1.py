from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/<data>')
def calcula_signo(data):
    lista_signos = ['Capricornio', 'Aquario', 'Peixes', 'Aries',
                    'Touro', 'Gemeos', 'Cancer', 'Leao', 'Virgem',
                    'Libra', 'Escorpiao', 'Sargitario', 'Capricornio']
    lista_datas = [121, 219, 321, 421, 521, 621, 723, 823, 923, 1023, 1122, 1222, 1231]

    # 14-03-1992 -> 314
    periodo = int(data[3:5] + data[:2])

    for i in lista_datas:
        if i > periodo:
            signo = lista_signos[lista_datas.index(i)]
            break
    return jsonify({'signo': signo})


app.run(host='0.0.0.0')