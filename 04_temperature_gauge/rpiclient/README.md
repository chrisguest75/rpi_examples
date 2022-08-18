# README

Create a client that uses RPI unicornhat and sends data to prometheus.

NOTES:  

* You'll need to ensure the `i2c` interface is enabled ```sudo raspi-config```  

## Start

```sh
pyenv local
pipenv install
pipenv shell
python ./main.py

python ./main.py --prometheus "http://0.0.0.0:8080"
python ./main.py --prometheus "http://0.0.0.0:8080" --plugin "plugin_random" --nic "en0"
python ./main.py --prometheus "http://0.0.0.0:8080" --plugin "plugin_rainbo
what"
python ./main.py --prometheus "http://192.168.1.222:9091" --plugin "plugin_rainbowhat"

```

## Docker

Build native.  

```sh
# build docker container
docker build -t temperature .  

# run docker container
docker run -it temperature python3 -u ./main.py --prometheus "http://host.docker.internal:8080" --plugin "plugin_random" --nic "eth0"

docker run -it temperature python3 -u ./main.py --prometheus "http://192.168.1.222:9091" --plugin "plugin_rainbowhat" --nic "eth0"
```

Build target arm64  

```sh
docker buildx build --platform linux/arm64 -t temperature_arm64 -f ./Dockerfile .
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

* pydron/ifaddr package [here](https://github.com/pydron/ifaddr)
* chrisguest75/wordament_solver_service [here](https://github.com/chrisguest75/wordament_solver_service)
* chrisguest75/py-wordament-helper [here](https://github.com/chrisguest75/py-wordament-helper)

https://github.com/chrisguest75/docker_examples/tree/master/56_pyenv_versions

