# virtualenv and run application
venv:
	virtualenv -p /usr/bin/python3 venv/ && \
    make venv_install_reqs && \
    make venv_install_reqs_dev

venv_bare:
    virtualenv -p /usr/bin/python3 venv_bare/

venv_install_reqs:
	. venv/bin/activate && \
    sudo apt-get install scrot && \
    sudo apt-get install python3-tk && \
    sudo apt-get install python3-dev && \
    pip install -r requirements.txt

venv_install_reqs_dev:
	. venv/bin/activate && pip install -r requirements_dev.txt

# tests and maintaining code
bandit:
	. venv/bin/activate && bandit -r app/*.py

black_all:
	. venv/bin/activate && black -l 119 -S app/ unittests/

test-unittests:
	. venv/bin/activate && \
	export PYTHONPATH=$PYTHONPATH:app/ && \
	python -m pytest app/ unittests/ -v -ra --cov --cov-report term-missing:skip-covered --pylama && \
	rm -r ".coverage" ".pytest_cache" "app/__pycache__" "unittests/__pycache__"
