# README

[![Repository](https://skillicons.dev/icons?i=linux,vscode)](https://skillicons.dev)

A repository for Raspberry PI examples  

## Prerequisites

Configure the following tools:

1. [pyenv-installer](https://github.com/pyenv/pyenv-installer)
1. [Pyenv](https://github.com/pyenv/pyenv)
1. [Intro to Pyenv](https://realpython.com/intro-to-pyenv/)
1. [Pipenv](https://realpython.com/pipenv-guide/)

```sh
sudo apt install libreadline-dev  
sudo apt install libbz2-dev  
sudo apt install libssl-dev   
sudo apt-get install libsqlite3-dev  
pyenv install 3.10.5  

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

## 01 - Webcam

Demonstrate how to get a webcam working.   
Steps [README.md](./01_webcam/README.md) 



