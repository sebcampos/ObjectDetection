# Linux commands

- `sudo iwlist scan` details about nearby wifi
- `sudo shutdown -h now` shuts down raspberry pi
- `bluetoothctl scan on` scan nearby bluetooth devices
- ```eval `ssh-agent -s` ``` starts ssh agent
- `lsb_release -dc` software version
- `uname -m` to see architecture
- ` uname -a` to see operating system
- 
###  Transfer files over SSH
- `scp /path/to/file username@a:/path/to/destination`
- `scp username@b:/path/to/file /path/to/destination`


# Setting up ubuntu (22.04 jammy)
- ssh agent
- sudo apt update
- sudo apt search vim
- sudo apt install vim

### Zsh and oh my zsh
- `apt install zsh`
- `sudo apt install curl wget git`
- `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
- `git clone https://github.com/zsh-users/zsh-syntax-highlighting`
- `echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc`
- `source ./zsh-syntax-highlighting/zsh-syntax-highlighting.zsh`


## Mongo
- not supported on jammy yet (https://jira.mongodb.org/browse/SERVER-62301)
- [dependency] `sudo apt-get install gnupg`
- `wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -`
- `echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list`


## Labeling Software
- git clone https://github.com/tzutalin/labelImg img_label_software


## pyenv
``https://realpython.com/intro-to-pyenv/``
### Pyenv dependencies
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

``` 
sudo apt update
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
zlib1g-dev \
libbluetooth-dev
```


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

# Tensorflow raspi 4 arm 64
All Object detection logic comes from Nicholas Renottes
5 hour Tensorflow Object Detection course on youtube

- `pip install tensorflow-aarch64`
- Annotation software `https://github.com/tzutalin/labelImg`



## Depencies

- `sudo install qtbase5-dev` before installing pyqt5
```
Package                      Version
---------------------------- -----------
absl-py                      1.0.0
asttokens                    2.0.5
astunparse                   1.6.3
backcall                     0.2.0
cachetools                   5.1.0
certifi                      2022.5.18.1
charset-normalizer           2.0.12
decorator                    5.1.1
dnspython                    2.2.1
executing                    0.8.3
flatbuffers                  1.12
gast                         0.4.0
google-auth                  2.6.6
google-auth-oauthlib         0.4.6
google-pasta                 0.2.0
grpcio                       1.46.3
h5py                         3.7.0
idna                         3.3
importlib-metadata           4.11.4
ipython                      8.3.0
jedi                         0.18.1
keras                        2.9.0
Keras-Preprocessing          1.1.2
libclang                     14.0.1
Markdown                     3.3.7
matplotlib-inline            0.1.3
numpy                        1.22.4
oauthlib                     3.2.0
opencv-python                4.5.5.64
opt-einsum                   3.3.0
packaging                    21.3
pandas                       1.4.2
parso                        0.8.3
pexpect                      4.8.0
pickleshare                  0.7.5
pip                          22.1.1
prompt-toolkit               3.0.29
protobuf                     3.20.1
ptyprocess                   0.7.0
pure-eval                    0.2.2
pyasn1                       0.4.8
pyasn1-modules               0.2.8
PyBluez			     0.23
Pygments                     2.12.0
pymongo                      4.1.1
pyparsing                    3.0.9
python-dateutil              2.8.2
pytz                         2022.1
requests                     2.27.1
requests-oauthlib            1.3.1
rsa                          4.8
setuptools                   49.2.1
six                          1.16.0
stack-data                   0.2.0
tensorboard                  2.9.0
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow-aarch64           2.9.0
tensorflow-estimator         2.9.0
tensorflow-io-gcs-filesystem 0.26.0
termcolor                    1.1.0
traitlets                    5.2.1.post0
typing_extensions            4.2.0
urllib3                      1.26.9
wcwidth                      0.2.5
Werkzeug                     2.1.2
wheel                        0.37.1
wrapt                        1.14.1
zipp                         3.8.0
```
