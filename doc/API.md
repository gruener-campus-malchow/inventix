Hier wird die Rest API geplant

# Muster der URI
https://inventix.gcm.schule/<API-Pfad>/<Parameter>

# Suchanfragen

## Suchanfrage Item (nach Name)
Verarbeitet Nutzeranfragen nach Name und gibt ein Feld von Items zurück, welches die Ergebnisse enthält.

- GET
- /search-items-by-name/{name_query}
- name_query = Nutzereingabe in das Suchfeld
- Antwort: JSON objekt mit array der möglichen Suchergebnisse und Anzahl
```js
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

## Suchanfrage Item (nach Tag ids)
Gibt Items aus der Datenbank aus, denen Tags der Suchanfrage zugeordnet sind.
Achtung! Parameter im Body, nicht in der URL senden!
- GET
- /search-items-by-tag-ids/
- Parameter (tag ids) im Request Body (JSON) als Array, wie folgt aufgebaut:
```js
{
    tags : [
        id_1, id_2, id_3, ..., id_n // as numbers
    ]
}
```
- tag_id = id des Tags. Keine Direkte Nutzerangabe sondern Auswahl von bestehender tags
- Antwort:
```js
{
	resultCount: number,
	results:
		[
			{
				name: string,
                id: number,
                tags: [
                    {
                        categoryName: string,
                        categoryId: number 
                    }
                ],
                // Additional Object Data
			},
			...
		]
}
```

## Suchanfrage Tag (nach Name)
Sucht nach Tags, die der Suchanfrage entsprechen.
- GET
- /search-tags-by-name/{name_query}
- name_query = Nutzereingabe in das Suchfeld
- Antwort:
```js
{
	resultCount: number,
	results:
		[
			{
				name: string,
                id: number,
                categoryName: string,
                categoryId: number, 
                // Additional Object Data
			},
			...
		]
}
```

## Liste der Tags nach Tag-Kategorie
Sucht nach Tags, die der gesuchten Kategorie entsprechen.
- GET
- /get-tags-by-category/{category_id}
- category_id = Id der Kategorie deren Tags gelistet werden sollen
- Antwort:
```js
{
	resultCount: number,
	tags : 
		[
			{
				name: string,
				id: number,
                categoryName: string,
                categoryId: number 
			},
			...
		]	
}
```

## Liste der existierenden Tags
Listet alle Tags auf.
- GET
- /get-all-tags
- Antwort:
```js
{
	resultCount: number,
	tags : 
		[
			{
				name: string,
				id: number,
                categoryName: string,
                categoryId: number 
			},
			...
		]	
}
```

## Liste der existierenden Tag-Kategorien
Listet alle existierenden Tagkategorien auf.
- GET
- /get-all-tag-categories
- Antwort:
```js
{
	resultCount: number,
	tagCategories : 
		[
			{
				name: string,
				id: number
			},
			...
		]	
}
```
