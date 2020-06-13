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
	* Users(id, vorname, nachname, mail, pwhash)
		* Fachbereich(id, longname, shortname)
		* FachbereichUser(id, Users_id, fb-name)
	* Items(id, name, notiz, visible_with_no_login, position_id, Users_id, Foto_id)
		* Position(id, Gebäude_id, Ort_id, kurzbezeichnung)
		* Foto(id, uri)
		* Gebäude(id, gebäudename) 	--> _FG1, FG2, TH FG2, ..._
		* Ort(id, name) 		--> _Garage 1, 3.202, 1.101 ..._








# Legende: #
##    Planned ##
## o: In progress ##
## ◎: Complete and untested ##
## ✔  : Complete and tested ##
