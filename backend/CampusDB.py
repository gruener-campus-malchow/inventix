import sqlite3


class db:
	def __init__(self):
		path = ""
		name = "campus_database"
		self.con = sqlite3.connect(path+name+".db")
		print("[CampusDB] Connected.")
		
		#self.execute(open("tables.sql","r").read())
		#self.getCursor().executescript(open("tables.sql","r").read())
		self.executescript(open("tables.sql","r").read())
	
	def getCursor(self):
		return self.con.cursor()
	
	def executescript(self,script):
		c = self.getCursor()
		c.executescript(script)
		self.con.commit()
	
	def execute(self, cmd):
		c = self.getCursor()
		c.execute(cmd)
		self.con.commit()
		
	def executeIn(self, cmd, insert):
		c = self.getCursor()
		c.execute(cmd, insert)
		self.con.commit()
		
	def select(self, cmd):
		c = self.getCursor()
		c.execute(cmd)
		return c.fetchall()
		
	def close(self):
		self.con.commit()
		self.con.close()
		print("[CampusDB] Connection closed.")
	
	def _getFachbereicheFromNutzer(self,nutzer_id):
		select = self.select("SELECT Fachbereich_id FROM FachbereichNutzer WHERE Nutzer_id == '"+str(nutzer_id)+"'")
		fbs = []
		print(select)
		if(len(select) > 0):
			for a in select:
				fb = self.select("SELECT * FROM Fachbereiche WHERE id == '"+str(a[0])+"'")
				if(len(fb) == 1):
					fbs.append(fb)
		return fbs
		
	def _getFachbereicheFromItem(self,item_id):
		select = self.select("SELECT Fachbereich_id FROM FachbereichItem WHERE Items_id == '"+str(item_id)+"'")
		fbs = []
		if(len(select) > 0):
			for a in select:
				fb = self.select("SELECT * FROM Fachbereiche WHERE id == '"+str(a)+"'")
				if(len(fb) == 1):
					fbs.append(fb)
		return fbs
	
	def _getTagsFromItem(self,item_id):
		select = self.select("SELECT Tags_id FROM TagItem WHERE Items_id == '"+str(item_id)+"'")
		fbs = []
		if(len(select) > 0):
			for a in select:
				fb = self.select("SELECT * FROM Tags WHERE id == '"+str(a)+"'")
				if(len(fb) == 1):
					fbs.append(fb)
		return fbs
		
	def getNutzerInfo(self,nutzer_id):
		select = self.select("SELECT * FROM Nutzer WHERE id == '"+str(nutzer_id)+"'")
		if(len(select) == 1):
			select = select[0]
			fachbereiche = self._getFachbereicheFromNutzer(select[0])
			return {"id":select[0],"vorname":select[1],"nachname":select[2],"mail":select[3],"fachbereiche":fachbereiche}
		return None
		
	def getNutzerID(self,nutzer_mail):
		select = self.select("SELECT id FROM Nutzer WHERE mail == '"+str(nutzer_mail)+"'")
		if(len(select) == 1):
			return select[0][0]
		return -1
		
	def checkPWHash(self,mail,pwhash):
		nutzerid = self.getNutzerID(mail)
		if(nutzerid >= 0):
			db_pwhash = self.select("SELECT pwhash FROM Nutzer WHERE id == '"+str(nutzerid)+"'")
			if(len(db_pwhash) == 1):
				return db_pwhash[0][0] == pwhash
		return False
		
	def getItemInfo(self,item_id):
		select = self.select("SELECT * FROM Items WHERE id == '"+str(item_id)+"'")
		if(len(select) == 1):
			s = select[0]
			fbs = self._getFachbereicheFromItem(s[0])
			tags = self._getTagsFromItem(s[0])
			return {"id":s[0],"name":s[1],"notiz":s[2],"visible_with_no_login":s[3],"position_id":s[4],"nutzer_id":s[5],"foto_id":s[6],"fachbereiche":fbs,"tags":tags}
		return None
		
	def getPositionInfo(self,position_id):
		select = self.select("SELECT * FROM Position WHERE id == '"+str(position_id)+"'")
		if(len(select) == 1):
			select = select[0]
			id = select[0]
			ortid = select[1]
			raumid = select[2]
			kbz = select[3]
			
			ortname = self.select("SELECT name FROM Ort WHERE id == '"+str(ortid)+"'")
			raumname = self.select("SELECT name FROM Raum WHERE id == '"+str(raumid)+"'")
			if len(ortname) == 1 and len(raumname) == 1:
				return {"id":id,"ort_name":ortname[0],"raum_name":raumname[0],"kurzbezeichnung":kbz}
			
		return None
		
	def getAllItems(self,ignore_visible=False):
		selection = self.select("SELECT id FROM Items" + stringHelper(ignore_visible,""," WHERE visible_with_no_login == '"+str(ignore_visible)+"'"))
		result = []
		for a in selection:
			item = self.getItemInfo(a[0][0])
			if item != None:
				result.append(item)
		return result
		
	def getAllNutzer(self):
		selection = self.select("SELECT id FROM Nutzer")
		result = []
		for a in selection:
			nutzer = self.getNutzerInfo(a[0])
			if nutzer != None:
				result.append(nutzer)
		return result
		
	def getAllTags(self):
		selection = self.select("SELECT tag FROM Tags")
		result = []
		for a in selection:
			result.append(a[0])
		return result
			
	def getAllFachbereiche(self):
		selection = self.select("SELECT * FROM Fachbereiche")
		return selection
		
	def getAllOrte(self):
		selection = self.select("SELECT name FROM Ort")
		return selection
		
	def getAllRaume(self):
		selection = self.select("SELECT name FROM Raum")
		return selection
		
	def addNutzer(self,vorname,nachname,mail,pwhash):
		select = self.select("SELECT * FROM Nutzer WHERE mail == '"+str(mail)+"'")
		if(len(select) == 0):
			self.executeIn("INSERT INTO Nutzer(vorname,nachname,mail,pwhash) VALUES(?,?,?,?)",(vorname,nachname,mail,pwhash))
			
			nutzerid = self.select("SELECT id FROM Nutzer WHERE mail == '"+str(mail)+"'")
			if(len(nutzerid) == 1):
				nutzerid = nutzerid[0]
				return {"success": True,"id":nutzerid}
				
		return {"success": False,"id":-1}
	
			
	def addFachbereich(self,longname,shortname):
		select = self.select("SELECT * FROM Fachbereiche WHERE longname == '"+str(longname)+"' AND shortname == '"+str(shortname)+"'")
		if(len(select) == 0):
			self.executeIn("INSERT INTO Fachbereiche(longname,shortname) VALUES(?,?)",(longname,shortname))
			
			fachid = self.select("SELECT id FROM Fachbereiche WHERE longname == '"+str(longname)+"' AND shortname == '"+str(shortname)+"'")
			
			if(len(fachid) == 1):
				fachid = fachid[0]
				return {"success": True,"id":fachid[0]}
				
		return {"success": False,"id":-1}
		
	def addFachbereichToNutzer(self,nutzer_id,fachbereich_id):
		try:
			self.executeIn("INSERT INTO FachbereichNutzer(Nutzer_id,Fachbereich_id) VALUES(?,?)",(nutzer_id,fachbereich_id))
			return {"success": True}
		except:
			return {"success": False}
	
	def addTag(self,name):
		select = self.select("SELECT * FROM Tags WHERE tag == '"+str(name)+"'")
		if(len(select) == 0):
			self.executeIn("INSERT INTO Tags(tag) VALUES(?)",(name,))
			
			tagid = self.select("SELECT id FROM Tags WHERE tag == '"+str(name)+"'")
			if(len(tagid) == 1):
				tagid = tagid[0]
				return {"success": True,"id":tagid}
				
		return {"success": False,"id":-1}
	
	
		
def stringHelper(statement, wahr, falsch):
	if(statement):
		return wahr
	return falsch
		
		
		
		
		
		
		
		