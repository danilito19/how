import csv
import urllib2
import sys


def get_rent_data(zipcode, metric):
    '''
    Gets data from
    https://www.quandl.com/blog/api-for-housing-data

    and returns the latest rent per square feet at the
    zip code

    inputs should be strings!

    '''
    quandl = 'http://www.quandl.com/api/v3/datasets/ZILL/Z' + zipcode + '_' + metric + '.csv'
    instructions = 'provide a valid zipcode and metric'

    try:
        response = urllib2.urlopen(quandl)
        cr = list(csv.reader(response))

        latest_rent = cr[1][1]
        return latest_rent

    except urllib2.HTTPError, e:
        print 'HTTPError = ' + str(e.code)
        print quandl
        print instructions
    except urllib2.URLError, e:
        print 'URLError = ' + str(e.reason)
        print quandl
        print instructions
    except httplib.HTTPException, e:
        print 'HTTPException'
        print quandl
        print instructions

    return 

if __name__=="__main__":
    instructions = '''Usage: file zip metric

                zipcode = '60615'
                metric = 'RZSF'
                    '''

    if(len(sys.argv) != 3):
        print(instructions)
        sys.exit()

    zipcode = sys.argv[1]
    metric = sys.argv[2]

    print get_rent_data(zipcode, metric)

