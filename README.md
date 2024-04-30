# Simple REST API

## Description

Das folgende Beispiel zeigt, wie man einen einfachen Webservice mit REST-API mit Python und Flask erstellt. Hierbei können Personen angelegt und deren Email-Adressen und andere Werte geändert oder hinzugefügt werden. Die Daten werden in der Datei `data.json` gespeichert.

## Requirements

```bash
pip install -r requirements.txt`
```

## Usage

- Starten des Severs mittels `python main.py`
- Dieser sollte nun unter `http://127.0.0.1:5000` erreichbar sein, Sie rufen diesen jedoch nicht im Browser auf, sondern strechen Sie die API mittels der bereitgestellten Python-Dateien an.
    - Mittels `post_api.py`können neue User angelegt werden
    - Mittels  `put_api.py` können Email-Adressen von Usern geändert oder hinzugefügt werden werden
    - Mittels `get_api.py` können Informationen zu Usern abgerufen werden
    - Mittels `delete_api.py` können User gelöscht werden

## API Endpoints


```
Methos   URI             : Description

GET 	/person          : Get all persons
POST 	/person          : Create a new person

GET 	/person/{name}   : Get the person information identified by "name"
PUT 	/person/{name}   : Update the person information identified by "name"
DELETE	/person/{name}   : Delete person by "name"
```