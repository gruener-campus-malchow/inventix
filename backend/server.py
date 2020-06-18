from flask import Flask
import CampusDB

app = Flask(__name__)
database = CampusDB.db()

if(True):
	database.addNutzer("Tim","Potter","mailzulang@zulang.com","#pwhashkoads")
	database.addNutzer("Kevin","Slavik","chantal@zulang.com","#pwhashkoadssdf")
	database.addNutzer("Apfel","Granger","little@zulang.com","#pwhashkoadsasdfg")
	
	fb1 = database.addFachbereich("Mathematik","Ma")["id"]
	fb2 = database.addFachbereich("Informatik","In")["id"]
	fb3 = database.addFachbereich("Physik","Phy")["id"]
	
	if(fb1 > 0):
		database.addFachbereichToNutzer(1,fb1)
		database.addFachbereichToNutzer(2,fb2)
		database.addFachbereichToNutzer(3,fb3)
	
	for nutzer in database.getAllNutzer():
		print("data:",nutzer, database.checkPWHash(nutzer["mail"],"#pwhashkoads"))
		
		
	database.addTag("Gefährlich")
	database.addTag("Giftig")
	database.addTag("Schleimig")
	database.addTag("Bunt")
	database.addTag("Rot")
	database.addTag("Blau")
	database.addTag("Schwarz")
	
	for tag in database.getAllTags():
		print("tags:",tag)
		
	for fb in database.getAllFachbereiche():
		print("fb:",fb)
	
@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
	
	
if __name__ == '__main__':
	try:
		app.run(port=8000)
	except:
		pass;
	database.close();