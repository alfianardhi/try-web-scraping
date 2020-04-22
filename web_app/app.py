import requests
from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        if (response.status_code == 200):
            json_datas = response.json()

            f = open('download/users_data.csv', 'w')
            f.write('No;Nama\n')
            for d in json_datas:
                tanggal = d['id']
                value = d['name']
                print(tanggal, ';', value)
                f.write('{};{}\n'.format(tanggal, value))
            f.close()

            return render_template('index.html', json_datas=json_datas)

    except Exception as ex:
        print(ex)

@app.route('/getDatas')
def getDatas():
    return render_template('index.html')

@app.route('/downloadUsers')
def downloadUsers():
    path = "../download/users_data.csv"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

##response = requests.get('https://jsonplaceholder.typicode.com/users')
#json_datas = {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}, {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}
##json_datas = response.json()
#print(json_datas)
"""for user in json_datas:
    print(user['id'])
    print(user['name'])
    print(user['username'])
    print(user['email'])
    print(user['address']['street'])
    print(user['address']['suite'])
    print(user['address']['city'])
    print(user['address']['zipcode'])
    print(user['phone'])
    print(user['website'])
    print(user['company']['name'])
    print(user['company']['catchPhrase'])
    print(user['company']['bs'])"""

