import requests
import numpy as np
import sys

def get_gas_price(zipcode):
    headers = {'Host': 'gasprices.mapquest.com',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Referer': 'http://gasprices.mapquest.com/'}
    url = 'http://gasprices.mapquest.com/services/v1/stations?filter=gasprice%3Aregular&sortby=distance&hits=10&offset=0&location=' + zipcode

    assert len(zipcode) == 5
    r = requests.get(url, headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print 'provide a correct zipcode'
        return "Error: " + str(e)

    results = r.json()['results']
    prices = []
    for i in results:
        gas = i["opisGasPrices"]
        for j in gas:
            if j['type'] == "Regular" and j['amount'] is not None:
                prices.append(float(j["amount"]))

    return np.mean(prices) if prices else None

if __name__=="__main__":
    instructions = '''Usage: file zip 

                zipcode = '60615'
                    '''

    if(len(sys.argv) != 2):
        print(instructions)
        sys.exit()

    zipcode = sys.argv[1]

    print get_gas_price(zipcode)
