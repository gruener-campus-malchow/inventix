# Inventix

Ein Inventursystem für den Grünen Campus Malchow


## ToDo-List ##
	
### Frontend: ###
* create header
	* with profile(-icon/button)
	* with search-bar
	* with add-item-button

### Backend: ###
* create webserver
* create api-requests
	* get Item with ID
	* search Item with Name(and more)
	* list all Items
	* add Item with configuration
* Register of New Users (Teachers only)
* Login for registered Users
* Database for
	* Nutzer(id, vorname, nachname, mail, pwhash) 										◎
		* Fachbereich(id, longname, shortname) 											◎
		* FachbereichNutzer(id, Nutzer_id, Fb-id) 										◎
	* Items(id, name, notiz, visible_with_no_login, Position_id, Nutzer_id, Foto_id) 	◎
		* FachbereichItem(id, Item_id, Fb-id) 											◎
		* Tag(id, tag) 																	◎
		* TagItem(id, Item_id, Tag_id) 													◎
		* Position(id, Ort_id, Raum_id, kurzbezeichnung) 								◎
		* Foto(id, uri)																	◎
		* Ort(id, name) 	--> _FG1, FG2, TH FG2, ..._									◎
		* Raum(id, name) 		--> _Garage 1, 3.202, 1.101, ..._						◎
#### Database-Functions: ####
	* getAllNutzer() -> [{id,vorname,nachname,mail,[fachbereiche]},...]
	* getNutzerInfo(nutzer_id) -> {id,vorname,nachname,mail,[fachbereiche]}
	* getAllItems(visible_with_no_login=False) -> [{id,name,notiz,visible_with_no_login,position_id,foto_id,[fachbereiche],[tags]},...]
	* getItemInfo(item_id) -> {id,name,notiz,visible_with_no_login,position_id,nutzer_id,foto_id,[fachbereiche],[tags]}
	* getPositionInfo(position_id) -> {id,ort_name,raum_name,kurzbezeichnung}






# Legende: #
##    Planned ##
## o: In progress ##
## ◎: Complete and untested ##
## ✔  : Complete and tested ##
