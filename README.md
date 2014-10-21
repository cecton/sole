sole
====

Smallest Odoo Lib Ever!

Synopsis
--------

```python
import sole

# connect
server = sole.connect("http://localhost:8069/xmlrpc", "DBNAME", "toto", "pwd")

# get a model
users = server('res.users')
for uid in users('search', []):
    print users('read', uid, [])

# get a method
search_partners = server('res.partner', 'search')
print "There are", \
      search_partners([], count=True), \
      "partner(s) on the database."
```
