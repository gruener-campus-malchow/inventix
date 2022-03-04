Hier wird die Rest API geplant

#Muster der URI
https://inventix.gcm.schule/<API-Pfad>/<Parameter>

#Suchanfragen

##Suchanfrage (Name)
- GET
- /search-by-name/{name_query}
- name_query = Nutzereingabe in das Suchfeld
- Antwort: JSON objekt mit array der möglichen Suchergebnisse und Anzahl
```
{
	resultCount: number,
	results:
		[
			{
				// Object Data
			},
			...
		]
}
```
