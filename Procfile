web: python manage.py collectstatic --noinput
web: python manage.py migrate
web: gunicorn hvccd12.wsgi --log-file -
heroku ps:scale web=1

