# Python

NOTE: I think I'm running out of memory building python

## Prequisites

```sh
# update indices
sudo apt update
sudo apt upgrade

# install required tools 
sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev liblzma-dev
```

## pyenv

```sh
cd ~
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# list versions
pyenv install --list

# both work (requires my 4gb pi)
pyenv install 3.8.13
pyenv install 3.10.6
```

## Configure

```sh
pyenv local 3.10.6
pyenv which python

# not sure about the sudo requirement here
sudo pip install pipenv

```


## Resources

* Install pyenv on Raspberry Pi and version control Python [here](https://www.linuxtut.com/en/c8b82ab42564256df884/)  
