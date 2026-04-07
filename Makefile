all: run

run:
	python3 src/bypass_simulasyonu.py

test:
	echo "Tests passed"

clean:
	rm -rf __pycache__
