sole
====

Smallest Odoo Lib Ever!

Synopsis
--------

```python
import sole

# connect
server = sole.connect("http://localhost:8069/xmlrpc", "DBNAME", "toto", "pwd")

# get a method
search_partners = server('res.partner', 'search')
print "There are", \
      search_partners([], count=True), \
      "partner(s) on the database."
```
