import sqlite3


class db:
	def __init__(self):
		path = ""
		name = "campus_database"
		self.con = sqlite3.connect(path+name+".db")
		
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
		
	def selectIn(self, cmd, insert):
		c = self.getCursor()
		c.execute(cmd,insert)
		return c.fetchall()
		
	def close(self):
		self.con.commit()
		self.con.close()