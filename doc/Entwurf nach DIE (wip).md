# API Entwurf nach DIE

## Items

```
      GET /items/		-> gibt liste mit allen items zurück
      GET /items/?color=red	-> gibt liste mit allen roten items zurück¹
      GET /items/42		-> gibt item #42 zurück
      GET /items/42/color	-> gibt farbe des items #42 zurück
*    HEAD *			-> wie GET, gibt aber keinen body zurück
     POST /items/		-> erstellt neues item aus dem request body, gibt id zurück
     POST /items/42		-> ändert existierendes item #42 mit daten aus dem request body²
*   PATCH /items/42		-> ändert existierendes item #42 mit daten aus dem request body²
      PUT /items/42		-> fügt item aus daten aus dem request body mit id 42 ein (ersetzt ggf. das alte)
*     PUT /items/		-> ersetzt alle items mit liste aus dem request body
   DELETE /items/42		-> löscht item #42
*  DELETE /items/		-> löscht alle items
* OPTIONS *			-> gibt http 402 mit allow header zurück
*       * /items		-> 400 Bad Request
*       * /items/42/		-> 400 Bad Request


```
## Tags

```
      GET /tags/		-> gibt liste mit allen tags zurück
      GET /tags/?status=approved	-> gibt tags mit dem Status 'approved' zurück
      GET /tags/42		-> gibt tags mit ID '42' zurück
      GET /tags/42/status	-> gibt status des tags #42 zurück
*    HEAD *			-> wie GET, gibt aber keinen body zurück
     POST /tags/		-> erstellt neues tag aus dem request body, gibt id zurück
     POST /tags/42		-> überschreibt existierendes tag #42 mit daten aus dem request body²
*   PATCH /tags/42		-> ändert existierendes item #42 mit daten aus dem request body²
      PUT /tags/42		-> fügt tag aus daten (aus dem request body) mit id 42 ein (ersetzt ggf. das alte) //benötigt Klärung, bitte
*     PUT /tags/		-> ersetzt alle tags mit liste aus dem request body
   DELETE /tags/42		-> löscht tag #42
*  DELETE /tags/		-> löscht alle tags
* OPTIONS *			-> gibt http 402 mit allow header zurück
*       * /items		-> 400 Bad Request
*       * /items/42/		-> 400 Bad Request


```

## Categories - ab hier dann weiterarbeiten

```
      GET /categories/		-> gibt liste mit allen categories zurück
      GET /categories/?name=farbe	-> gibt liste mit allen // die restlichen GETs löschen?
      GET /items/42		-> gibt item #42 zurück
      GET /items/42/color	-> gibt farbe des items #42 zurück
*    HEAD *			-> wie GET, gibt aber keinen body zurück
     POST /items/		-> erstellt neues item aus dem request body, gibt id zurück
     POST /items/42		-> ändert existierendes item #42 mit daten aus dem request body²
*   PATCH /items/42		-> ändert existierendes item #42 mit daten aus dem request body²
      PUT /items/42		-> fügt item aus daten aus dem request body mit id 42 ein (ersetzt ggf. das alte)
*     PUT /items/		-> ersetzt alle items mit liste aus dem request body
   DELETE /items/42		-> löscht item #42
*  DELETE /items/		-> löscht alle items
* OPTIONS *			-> gibt http 402 mit allow header zurück
*       * /items		-> 400 Bad Request
*       * /items/42/		-> 400 Bad Request


```


## Users

```
      GET /items/		-> gibt liste mit allen items zurück
      GET /items/?color=red	-> gibt liste mit allen roten items zurück¹
      GET /items/42		-> gibt item #42 zurück
      GET /items/42/color	-> gibt farbe des items #42 zurück
*    HEAD *			-> wie GET, gibt aber keinen body zurück
     POST /items/		-> erstellt neues item aus dem request body, gibt id zurück
     POST /items/42		-> ändert existierendes item #42 mit daten aus dem request body²
*   PATCH /items/42		-> ändert existierendes item #42 mit daten aus dem request body²
      PUT /items/42		-> fügt item aus daten aus dem request body mit id 42 ein (ersetzt ggf. das alte)
*     PUT /items/		-> ersetzt alle items mit liste aus dem request body
   DELETE /items/42		-> löscht item #42
*  DELETE /items/		-> löscht alle items
* OPTIONS *			-> gibt http 402 mit allow header zurück
*       * /items		-> 400 Bad Request
*       * /items/42/		-> 400 Bad Request


```
