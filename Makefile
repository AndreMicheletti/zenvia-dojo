
default:
	@ echo "usage: make [run-docker/run-tests]"

run-docker:
	@ docker build -t zenvia_dojo .
	@ docker run -it zenvia_dojo

run-tests:
	@ pytest -x --cov=romanos --cov-report=term
