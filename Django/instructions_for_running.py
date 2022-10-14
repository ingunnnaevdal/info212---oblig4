"""
How to run the server in the terminal:

# To create:
python3 -m virtualenv django-test
cd django-test
py3 scripts/activate
pip3 install django
pip3 install djangorestframework
django-admin startproject mysite
cd mysite
python manage.py runserver

# To start server after creation
python manage.py runserver

# To deactivate virtual environment:
deactivate


"""

# Bugs that has happened:
"""
Run this script:
    python manage.py makemigrations
    python manage.py migrate
    
If not working try this:
    manage.py migrate --run-syncdb
    
For further issues try this link:
https://stackoverflow.com/questions/34548768/no-such-table-exception

Sometimes deleting the sql-database helps. 
"""