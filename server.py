from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('contacts.txt', mode='a') as db:
        email = data['from']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('db.csv', mode='a', newline = '') as csv_db:
        email = data['from']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            'did not save to db'
    else:
        return 'something went wrong with the form'
