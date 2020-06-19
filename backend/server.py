from flask import Flask
import CampusDB

app = Flask(__name__)
database = CampusDB.db()

if(True):
	n1 = database.addNutzer("Tim","Potter","mailzulang@zulang.com","#pwhashkoads")
	n2 = database.addNutzer("Kevin","Slavik","chantal@zulang.com","#pwhashkoadssdf")
	n3 = database.addNutzer("Apfel","Granger","little@zulang.com","#pwhashkoadsasdfg")
	print("nutzer-stats:",n1,n2,n3)
	
	fb1 = database.addFachbereich("Mathematik","Ma")["id"]
	fb2 = database.addFachbereich("Informatik","In")["id"]
	fb3 = database.addFachbereich("Physik","Phy")["id"]
	print("fb-id:",fb1,fb2,fb3)
	
	for fb in database.getAllFachbereiche():
		print("fb:",fb)
	
	if(fb1 > 0):
		database.addFachbereichToNutzer(1,fb1)
		database.addFachbereichToNutzer(2,fb2)
		database.addFachbereichToNutzer(3,fb3)
	
	for nutzer in database.getAllNutzer():
		print("nutzer:",nutzer, database.checkPWHash(nutzer["mail"],"#pwhashkoads"))
		
		
	t1 = database.addTag("Gefährlich")
	t2 = database.addTag("Giftig")
	t3 = database.addTag("Schleimig")
	t4 = database.addTag("Bunt")
	t5 = database.addTag("Rot")
	t6 = database.addTag("Blau")
	t7 = database.addTag("Schwarz")
	print("tag-stats:",t1,t2,t3,t4,t5,t6,t7)
	
	for tag in database.getAllTags():
		print("tags:",tag)
		
	
		
	f1 = database.addFoto("items/data/sda4sdf65d4fas5d4fs.png")
	f2 = database.addFoto("items/data/automatpicture.png")
	f3 = database.addFoto("items/data/gluebirnepicture.png")
	print("foto-stats:",f1,f2,f3)
	
	for foto in database.getAllFotos():
		print("uri:",foto)
		
	o1 = database.addOrt("HG")
	o2 = database.addOrt("FG I")
	o3 = database.addOrt("FG II")
	o4 = database.addOrt("FG III")
	o5 = database.addOrt("TH-FG II")
	print("ort-stats:",o1,o2,o3,o4,o5)
	
	for ort in database.getAllOrte():
		print("Ort:",ort)
		
	r1 = database.addRaum("202")
	r2 = database.addRaum("307")
	r3 = database.addRaum("107")
	print("raum-stats:",r1,r2,r3)
	
	for raum in database.getAllRaume():
		print("Raum:",raum)
	
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