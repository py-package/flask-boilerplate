upgrade:
	flask db upgrade

downgrade:
	flask db downgrade

start:
	gunicorn -w 4 wsgi:app -t 90 -b 0.0.0.0:5000 --reload