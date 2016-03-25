from flask import Flask, jsonify, render_template, request
from data import load_gas_data, load_rent_data
import calc_best

app = Flask(__name__)

@app.route('/')
def index():
    #get user input, zips
    #pass zips into
    #pick zip for gas depending on which radio dial is selected
    #check that user provided all information
    # home_rent = load_rent_data.get_rent_data('60615', 'RMP')
    # work_rent = load_rent_data.get_rent_data('60601', 'RMP')
    # gas_price = load_gas_data.get_gas_price('60615')
    #print calc_best(home_rent, work_rent, gas_price, 10, 10)

    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    home = 'at home'
    work = 'near work'

    output = '''With your current rent, commute, and gas prices, 
                we estimate you're better off living''' + home 

    print request.args
    print 'this is home zip'
    home_zip = request.args.get('home_zip', 'nothing')
    print home_zip


    return jsonify(request.args)


if __name__ == '__main__':
    app.run(debug=True)