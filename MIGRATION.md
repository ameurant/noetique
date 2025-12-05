## noetique.site.Book

### EXPORT DES LIVRES : problème avec l'attribut *filename* du champ *cover* qui est None

```
2025-08-27 14:21:54 ERROR collective.exportimport.export_content Error exporting https://noetique.eu/livres/traite-sens-vie
Traceback (most recent call last):
  File "/data/eggs/collective.exportimport-1.12-py2.7.egg/collective/exportimport/export_content.py", line 372, in export_content
    item = serializer()
  File "/data/eggs/plone.restapi-7.9.1-py2.7.egg/plone/restapi/serializer/dxcontent.py", line 103, in __call__
    value = serializer()
  File "/data/eggs/collective.exportimport-1.12-py2.7.egg/collective/exportimport/serializer.py", line 93, in __call__
    if "built-in function id" in namedfile.filename:
TypeError: argument of type 'NoneType' is not iterable
```

##### FIX

Changer la ligne  93 de collective.exportimport.serializer.py

if **namedfile.filename and** "built-in function id" in namedfile.filename:

### IMPORT DES LIVRES

    2025-08-27 15:25:32,456 WARNING [collective.exportimport.import_content:497][waitress-1] Cannot deserialize noetique.Book https://noetique.eu/livres/kabbale-theosophique
    Traceback (most recent call last):
    File "/Users/sverbois/plone/noetique/eggs/collective.exportimport-1.15-py3.12.egg/collective/exportimport/import_content.py", line 489, in handle_new_object
        new = deserializer(validate_all=False, data=item)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/sverbois/plone/noetique/eggs/plone.restapi-9.15.1-py3.12.egg/plone/restapi/deserializer/dxcontent.py", line 63, in __call__
        raise BadRequest(errors)
    zExceptions.BadRequest: [{'message': 'Contrainte non satisfaite', 'field': 'audience', 'error': 'ValidationError'}]
    2025-08-27 15:25:32,469 WARNING [collective.exportimport.import_content:473][waitress-1] [{'message': 'Contrainte non satisfaite', 'field': 'audience', 'error': 'ValidationError'}]
    2025-08-27 15:25:32,469 WARNING [collective.exportimport.import_content:474][waitress-1] Didn't add noetique.Book https://noetique.eu/livres/kabbale-theosophique
    Traceback (most recent call last):
    File "/Users/sverbois/plone/noetique/eggs/collective.exportimport-1.15-py3.12.egg/collective/exportimport/import_content.py", line 464, in import_new_content
        new = self.handle_new_object(item, index, new)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/sverbois/plone/noetique/eggs/collective.exportimport-1.15-py3.12.egg/collective/exportimport/import_content.py", line 489, in handle_new_object
        new = deserializer(validate_all=False, data=item)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/sverbois/plone/noetique/eggs/plone.restapi-9.15.1-py3.12.egg/plone/restapi/deserializer/dxcontent.py", line 63, in __call__
        raise BadRequest(errors)
    zExceptions.BadRequest: [{'message': 'Contrainte non satisfaite', 'field': 'audience', 'error': 'ValidationError'}]

## EXPORT JOURNAL

OK

## IMPORT JOURNAL

Il faut supprimer la langue "fr-be"

  "language": "fr-be",  ==> "language": "",