# Linux commands

- `sudo iwlist scan` details about nearby wifi
- `sudo shutdown -h now` shuts down raspberry pi
- `bluetoothctl scan on` scan nearby bluetooth devices
- ```eval `ssh-agent -s` ``` starts ssh agent
- `lsb_release -dc` software version

# Windows commands
- `netsh wlan show profile <arg>`

# Setting up ubuntu (22.04 jammy)
- ssh agent
- sudo apt update
- sudo apt search vim
- sudo apt install vim


## Mongo
- not supported on jammy yet (https://jira.mongodb.org/browse/SERVER-62301)
- [dependency] `sudo apt-get install gnupg`
- `wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -`
- `echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list`

## Zsh and oh my zsh
- `apt install zsh`
- `sudo apt install curl wget git`
- `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- `git clone https://github.com/zsh-users/zsh-syntax-highlighting`
- `echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc`
- `source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh`


## pyenv
``https://realpython.com/intro-to-pyenv/``
### Pyenv dependencies
- sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
  libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
- sudo apt update
  sudo apt install \
  build-essential \
  curl \
  libbz2-dev \
  libffi-dev \
  liblzma-dev \
  libncursesw5-dev \
  libreadline-dev \
  libsqlite3-dev \
  libssl-dev \
  libxml2-dev \
  libxmlsec1-dev \
  llvm \
  make \
  tk-dev \
  wget \
  xz-utils \
  zlib1g-dev


### Install script
- curl https://pyenv.run | bash
```
WARNING: seems you still have not added 'pyenv' to the load path.

Load pyenv automatically by adding
the following to ~/.bashrc:

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
### Create different versions and venvs
- pyenv local \*.\*.*
- pyenv virtualenv <python_version> <environment_name>
- pyenv local <environment_name>

## tensorflow raspi 4 arm 64
-  ` pip install tensorflow-aarch64`
