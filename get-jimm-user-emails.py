import json
import sys
import requests
import pandas
import subprocess

# run jupyter notebook export of data frame to the CSV file first
JIMM_USER_FILE = 'jimm-users.csv'
CANDID_USER_URL = 'https://api.jujucharms.com/identity/v1/u/'


df = pandas.read_csv('jimm-users.csv')

data = []

users = df[['owner', 'created']]

for index, row in users.iterrows():
    user = row['owner'] 
    models = row['created']
    print(user, models)
    url = CANDID_USER_URL+user
    result = subprocess.run(['bhttp', url, '--raw'], stdout=subprocess.PIPE)
    user_raw = result.stdout.decode('utf-8')
    print(user_raw)
    user_data = json.loads(user_raw)
    if not 'message' in user_data:
        full_name = ""
        if 'fullname' in user_data:
            full_name = user_data['fullname']
        email = user_data['email']
        last_login = user_data['last_login']
        last_interaction = user_data['last_discharge']

        data.append([user, full_name, email, last_login, last_interaction, models])

columns = ['user', 'fullname','email', 'last_login', 'last_interaction', 'models']
alldf = pandas.DataFrame(data, columns=columns)
print(alldf)

f = open('jimm-user-emails.csv', 'w')
f.write(alldf.to_csv())
