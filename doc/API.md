Hier wird die Rest API geplant

# Muster der URI
https://inventix.org/{API-Pfad}/{Parameter}

# Suchanfragen

## Suchanfrage Item (nach Name)
Verarbeitet Nutzeranfragen nach Name und gibt ein Feld von Items zurück, welches die Ergebnisse enthält.

- GET
- ``/search-items-by-name/{name_query}``
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
                    qrCodeUrl: string
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
- ``/search-items-by-tag-ids/``
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
                            categoryId: number,
                            synonyms: [ "", "", ... ]
                        }
                    ],
                    qrCodeUrl: string
                    // Additional Object Data
			    },
			    ...
		    ]
    }
```

## Suchanfrage Tag (nach Name)
Sucht nach Tags, die der Suchanfrage entsprechen.

- GET
- ``/search-tags-by-name/{name_query}``
- name_query = Nutzereingabe in das Suchfeld
- Antwort:
```js
    {
	    resultCount: number,
	    results:
		    [
			    {
				    name: string,
                    synonyms: [ "", "", ... ],
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
Sucht nach Tags, die der gesuchten Kategorie entsprechen. Ein Item kann nur einen Tag einer Kategorie enthalten.
Beispielkategorien: 
- Zustand (neuwertig, defekt, ...), 
- Raum (Raumnummer), 
- Schrank (Schranknummer, Fach o.Ä.), 
- Schulfach (Physik, Mathematik, ...)
- Gegenstandstyp (Buch, Experimentiermaterial, ...) 

**Anfrage**
- GET
- ``/get-tags-by-category/{category_id}``
- category_id = Id der Kategorie deren Tags gelistet werden sollen
- Antwort:
```js
    {
	    resultCount: number,
	    tags : 
		    [
			    {
				    name: string,
                    synonyms: [ "", "", ... ]
				    id: number,
                    categoryName: string,
                    categoryId: number 
			    },
			    ...
		    ]	
    }
```

## Liste der existierenden Tags
Listet alle verfügbaren Tags auf.

- GET
- ``/get-all-tags``
- Antwort:
```js
    {
	    resultCount: number,
	    tags : 
		    [
			    {
				    name: string,
				    id: number,
                    synonyms: [ "", "", ... ],
                    categoryName: string,
                    categoryId: number 
			    },
			    ...
		    ]	
    }
```

## Liste der von Usern vorgeschlagenen Tags (nur Admin)
Listet alle Tags auf, die noch nicht von einem Admin bestätigt oder verworfen wurden und die eventuell zugelassen werden.

- GET
- ``/get-suggested-tags``
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
Listet alle existierenden und verfügbaren Tagkategorien auf.

- GET
- ``/get-all-tag-categories``
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

# Create-Funktionalitäten

## Anlegen eines Items
Erstellt ein neues item in der Datenbank und weist diesem verschiedene Werte zu.
Achtung! Parameter im Body, nicht in der URL senden!
- POST
- ``/create-item``
- Parameter des neuen Items im Request Body (JSON), wie folgt aufgebaut:
```js
    {
        name: string,
        description: string,
        tags : [
            id_1, id_2, id_3, ..., id_n // as numbers
        ],
        // Additional Object Data
    }
```

## Anlegen eines Tags (nur Admin)
Erstellt ein neues Tag in der Datenbank, welchen Items zugewiesen werden kann.
Achtung! Parameter im Body, nicht in der URL senden!
- POST
- ``/create-tag``
- Parameter des neuen Items im Request Body (JSON), wie folgt aufgebaut:
```js
    {
        name: string,
        synonyms: ["", "", "", ...]
        description: string,
        categoryId : number
    }
```

## Anlegen (bzw. Vorschlagen) eines Tags (Standarduser)
Möglichkeit ein neues Tag vorzuschlagen. Muss erst von einem Admin genehmigt werden, damit es verwendet und gelistet werden kann.
Achtung! Parameter im Body, nicht in der URL senden!
- POST
- ``/create-tag-suggestion``
- Parameter des neuen Items im Request Body (JSON), wie folgt aufgebaut:
```js
    {
        name: string,
        synonyms: ["", ""],
        description: string,
        categoryId : number
    }
```

# Update-Funktionalitäten

## Aktualisieren eines Itemdatensatzes
Achtung! Zusätzliche Parameter im Body!
- PUT
- ``/update-item/{item_id}``
- Aktualisierte Datensätze des Items im Request Body (JSON), wie folgt aufgebaut. Alle Parameter sind optional, nur zu verändernde Datensätze müssen übertragen werden.
```js
    {
        name: string,
        description: string,
        tags : [
            id_1, id_2, id_3, ..., id_n // as numbers
        ],
        // Additional Object Data
    }
```

## Aktualisieren eines Tag-Datensatzes
Achtung! Zusätzliche Parameter im Body!
- PUT
- ``/update-tag/{tag_id}``
- tag_id - Id des zu verändernden Tags
- Aktualisierte Parameter des Tags im Request Body (JSON), wie folgt aufgebaut. Alle Parameter sind optional, nur zu verändernde Datensätze müssen übertragen werden.
```js
{
    name: string,
    synonyms: ["", "", "", ...]
    description: string,
    categoryId : number
}
```

## Bestätigen eines vorgeschlagenen Nutzer-Tags (nur Admin)
Bestätigt einen einzelnen Tag der von Nutzern vorgeschlagen wurde.
- PUT
- ``/approve-tag/{tag_id}search-items-by-name/{name_query}``
name_query = Nutzereingabe in das search-items-by-name/{name_query}
name_query = Nutzereingabe in das 

# Delete-Funktionalitäten

## Löschen eines Tags (nur Admin)
Löscht ein Tag.
- DELETE
- ``/delete-tag/{tag_id}``
- tag_id = id des Tags

## Löschen eines Items (nur Admin)
Entfernt ein Item von der Datenbank.
- DELETE
- ``/delete-item/{item_id}``
- item_id = id des Items
