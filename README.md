# Django_url_test_task

Implement URL Status Checker
Django project git repository with application code that:

- Allow store and manipulate with a set of URLs (stored in DB, using Django ORM), manipulation (add/delete) via Django admin.
- Simple view for authenticated users, that shows a list of added URLs, monitors URL HTTP response status (using Ajax request to the server), let's choose to check interval, pause individual links check
- On ajax request, the server should check (in async) all user's links listed in DB and return the HTTP status code of URLs (200 - green row in the list, other - red row in the list).
