setup:
	sudo apt-get install python3
	sudo apt-get install python3-pip
	pip3 install graphviz
	sudo apt-get install xdg-utils

clean:
	rm output*

run:
	python3 minsky.py $(csv)
	xdg-open output.pdf
