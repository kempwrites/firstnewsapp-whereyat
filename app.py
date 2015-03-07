import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = "./static/la-riots-deaths.csv"
	csv_file = open(csv_path, 'r')
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list


@app.route('/<row_id>')
def detail(row_id):
	template = 'detail.html'
	object_list = get_csv()
	return render_template(template, object_list=object_list)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
