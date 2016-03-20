from flask import Flask, render_template
from data import load_gas_data, load_rent_data
import calc_best

app = Flask(__name__)


@app.route('/')
def index():
    #get user input, zips
    #pass zips into
    # home_rent = load_rent_data.get_rent_data('60615', 'RMP')
    # work_rent = load_rent_data.get_rent_data('60601', 'RMP')
    # gas_price = load_gas_data.get_gas_price('60615')
    #print calc_best(home_rent, work_rent, gas_price, 10, 10)

    return render_template('index.html')
def results():
    pass

if __name__ == '__main__':
    app.run(debug=True)