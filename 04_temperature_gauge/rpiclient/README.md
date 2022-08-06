# README

Create a client that uses RPI unicornhat and sends data to prometheus.

## Start

```sh
pyenv local
pipenv install
pipenv shell
python ./main.py

python ./main.py --prometheus "http://0.0.0.0:8080"
```

## Created

```sh
export PIPENV_VENV_IN_PROJECT=1
pyenv install --list
pipenv install --three
pipenv shell
pyenv local

pipenv install ptvsd python-json-logger      
pipenv install requests   
pipenv install --dev flake8   
```

## Resources

https://github.com/chrisguest75/wordament_solver_service
https://github.com/chrisguest75/py-wordament-helper
https://github.com/chrisguest75/docker_examples/tree/master/56_pyenv_versions

https://github.com/pydron/ifaddr