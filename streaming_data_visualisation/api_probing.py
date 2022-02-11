import requests as req
from pprintpp import pprint
from time import sleep


URL = 'http://127.0.0.1:5000/'

while True:
    sleep(0.2)
    res = req.get(URL)
    pprint(res.text)
