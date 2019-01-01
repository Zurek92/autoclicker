# virtualenv and run application
install_dependencies:
	sudo apt-get install scrot && \
	sudo apt-get install python3-tk && \
	sudo apt-get install python3-dev

venv:
	virtualenv -p /usr/bin/python3 venv/ && \
	make venv_install_reqs && \
	make venv_install_reqs_dev

venv_bare:
	virtualenv -p /usr/bin/python3 venv_bare/

venv_install_reqs:
	. venv/bin/activate && \
	pip install -r requirements.txt

venv_install_reqs_dev:
	. venv/bin/activate && pip install -r requirements_dev.txt

# tests and maintaining code
bandit:
	. venv/bin/activate && bandit -r autoclicker/*.py

black_all:
	. venv/bin/activate && black -l 119 -S autoclicker/ unittests/

test-unittests:
	. venv/bin/activate && \
	export PYTHONPATH=$PYTHONPATH:autoclicker/ && \
	python -m pytest autoclicker/ unittests/ -v -ra -s --cov --cov-report term-missing --pylama && \
	rm -r ".coverage" ".pytest_cache" "autoclicker/__pycache__" "unittests/__pycache__"
