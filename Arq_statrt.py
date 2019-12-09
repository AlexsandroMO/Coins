import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import lxml
import json
import requests
import re

url = 'http://fipeapi.appspot.com/api/1/carros/marcas.json'
print(url)
r = requests.get(url)
print(r)
