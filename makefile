virtual-env:
	conda create -n twtapp python=3.9

install:
	make virtual-env
	source activate twtapp
	pip install -r requirements.txt

run:
	python3 main.py

app:
	python3 app.py