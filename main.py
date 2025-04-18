from flask import Flask, render_template, request
app = Flask(__name__)

def calcular_vpl(receita, custo, anos, taxa_desconto, valor_residual):
    try:
        receita = float(receita.replace(",", "."))
        custo = float(custo.replace(",", "."))
        anos = int(anos)
        taxa = float(taxa_desconto.replace(",", ".")) / 100
        valor_residual = float(valor_residual.replace(",", "."))

        vpl = 0
        for t in range(1, anos + 1):
            fluxo = receita - custo
            vpl += fluxo / ((1 + taxa) ** t)
        vpl += valor_residual / ((1 + taxa) ** anos)
        return round(vpl, 2)
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        dados = request.form
        resultado = calcular_vpl(
            dados.get('receita'), dados.get('custo'),
            dados.get('anos'), dados.get('taxa'),
            dados.get('residual')
        )
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
