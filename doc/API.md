Hier wird die Rest API geplant

#Muster der URI
https://inventix.gcm.schule/<API-Pfad>/<Parameter>

#Suchanfragen

##Suchanfrage Item (nach Name)
Verarbeitet Nutzeranfragen nach Name und gibt ein Feld von Items zurück, welches die Ergebnisse enthält.

- GET
- /search-items-by-name/{name_query}
- name_query = Nutzereingabe in das Suchfeld
- Antwort: JSON objekt mit array der möglichen Suchergebnisse und Anzahl
```json
{
	resultCount: number,
	results:
		[
			{
				name: string,
                id: number,
                tags: [],
                // Additional Object Data
			},
			...
		]
}
```

##Suchanfrage Item (nach Tag id)
Gibt Items aus der Datenbank aus, denen Tags der Suchanfrage zugeordnet sind.
Achtung! Parameter im Body, nicht in der URL senden!
- GET
- /search-items-by-tag-ids/
- Parameter (tag ids) im Request Body (JSON) als Array, wie folgt aufgebaut:
```json
{
    tags : [
        id_1, id_2, id_3, ..., id_n // as numbers
    ]
}
```
- tag_id = id des Tags. Keine Direkte Nutzerangabe sondern Auswahl von bestehender tags
- Antwort:
```json
{
	resultCount: number,
	results:
		[
			{
				name: string,
                id: number,
                tags: [],
                // Additional Object Data
			},
			...
		]
}
```

##Suchanfrage Tag (nach Name)
- GET
- /search-tags-by-name/{name_query}
- name_query = Nutzereingabe in das Suchfeld

##Liste der existierenden Tags
- GET
- /get-all-tags
- Antwort:
```json
{
	resultCount: number,
	tags : 
		[
			{
				name: string,
				id: number
			},
			...
		]	
}
```
