import os

def get_path():
    return '%s/%s' % (os.path.dirname(__file__), 'GeoLiteCity.dat')
