from flask import Flask, render_template, request
import re
import json
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    components = analyze_expression(expression)
    result = evaluate_expression(expression)
    # Generar la data del árbol y pasarla como string JSON
    tree_data = generate_syntax_tree(expression)
    return render_template('calculator.html', components=components, result=result, tree_data=json.dumps(tree_data))

def analyze_expression(expression):
    operators = {'+': 'Suma', '-': 'Resta', '*': 'Multiplicación', '/': 'División', '(': 'Paréntesis de apertura', ')': 'Paréntesis de cierre'}
    components = re.findall(r'\d+|[()+\-*/]', expression)
    analyzed_components = []
    for component in components:
        if component.isdigit():
            analyzed_components.append((component, 'Número'))
        else:
            analyzed_components.append((component, operators.get(component, 'Operador')))
    return analyzed_components

def evaluate_expression(expression):
    expression = expression.replace('^', '**')
    return eval(expression, {'__builtins__': None}, {'math': math})

def generate_syntax_tree(expression):
    # Usar math.js para analizar la expresión y obtener el árbol sintáctico
    # Esta implementación asume que tienes math.js en tu directorio static/js/
    return {"nodes": [{"id": 1, "label": "Raíz"}], "edges": []}

if __name__ == '__main__':
    app.run(debug=True)
