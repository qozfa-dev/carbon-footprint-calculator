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
    error = None
    if request.method == 'POST':
        product = request.form['product'].strip().lower()
        weight_input = request.form['weight'].strip()
        distance_input = request.form['distance'].strip()

        if not product or not weight_input or not distance_input:
            error = "Please fill in all the fields."
        else:
            try:
                weight = float(weight_input)
                distance = float(distance_input)

                if product in EMISSION_FACTORS:
                    emissions = weight * EMISSION_FACTORS[product]
                    emissions += (distance * 0.1)
                    result = round(emissions, 2)
                else:
                    result = "Product is not valid"

            except ValueError:
                error = "The weight and distance must be valid numbers."

    return render_template('index.html', result=result, error=error)


if __name__ == '__main__':
    app.run(debug=True)
