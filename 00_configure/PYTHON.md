# Python

NOTE: I think I'm running out of memory building python


```sh
sudo apt update
sudo apt upgrade
sudo apt install -y git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev
```


```sh
cd ~
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"


pyenv install --list

# works
pyenv install 3.8.13

# does not work
pyenv install 3.6.15

https://github.com/pyenv/pyenv/issues/1621
pyenv install 3.10.6
```


## Resources

* Install pyenv on Raspberry Pi and version control Python [here](https://www.linuxtut.com/en/c8b82ab42564256df884/)