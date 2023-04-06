setup:
	pipenv install && pipenv shell

run: 
	python app.py

test:
	pytest program -vv
