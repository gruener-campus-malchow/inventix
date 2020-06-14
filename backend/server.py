from flask import Flask
import CampusDB

app = Flask(__name__)
database = CampusDB.db()


@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
	
	
if __name__ == '__main__':
	app.run(port=8000)