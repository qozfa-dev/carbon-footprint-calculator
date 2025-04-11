from flask import Flask, render_template, request

app = Flask(__name__)

# Basic emission factors for some items
EMISSION_FACTORS = {
    'apple': 0.5,   # kg CO2 per kg of apple
    'chicken': 6.0,
    'carrot': 0.4,
    'beef': 27.0,
    'banana': 0.3,
}


@app.route('/', methods=['GET', 'POST'])
def login():
    result = None
    if request.method == 'POST':
        product = request.form['product'].lower()
        weight = float(request.form['weight'])
        distance = float(request.form['distance'])

        if product in EMISSION_FACTORS:
            emissions = weight * EMISSION_FACTORS[product]
            emissions += (distance * 0.1)

            result = round(emissions, 2)
        else:
            result = "Product is not valid"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
