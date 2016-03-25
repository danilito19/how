from flask import Flask, jsonify, render_template, request
from data import load_gas_data, load_rent_data
from calc_best import calc_best

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    home = 'at home'
    work = 'near work'

    output = '''With your current rent, commute, and gas prices, 
                we estimate you're better off living'''

    print 'ARGS', request.args
    home_zip = str(request.args.get('home_zip'))
    work_zip = str(request.args.get('work_zip'))
    miles = int(request.args.get('miles'))
    mpg = int(request.args.get('mpg'))

    # pick zip for gas depending on which radio dial is selected
    # check that user provided all information
    if request.args.get('radio') == 'home':
        gas_price = load_gas_data.get_gas_price(home_zip)
    else:
        gas_price = load_gas_data.get_gas_price(work_zip)

    home_rent = load_rent_data.get_rent_data(home_zip, 'RMP')
    work_rent = load_rent_data.get_rent_data(work_zip, 'RMP')
    decision = calc_best(home_rent, work_rent, gas_price, miles, mpg)


    if decision:
        return render_template('results.html', decision = output + home)
    else:
        return render_template('results.html', decision = output + work)
    #return jsonify(request.args)


if __name__ == '__main__':
    app.run(debug=True)