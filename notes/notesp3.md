https://forums.raspberrypi.com/viewtopic.php?t=305186

# Rasp
- tensorflow (pip install tensorflow-aarch64)
- ipython
- `uname -m` to see architecture
- ` uname -a` to see operating system

# Pyenv to manage different verions of python
- https://realpython.com/intro-to-pyenv/#installing-pyenv
- install dependancies first `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev`
- lscpu

# Transfer files over SSH
- `scp /path/to/file username@a:/path/to/destination`
- `scp username@b:/path/to/file /path/to/destination`

# set up for tensorflow raspi 4
-  tensorflow-aarch64


# Mongo installation for Raspberry PI
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
# Add the source location for the MongoDB packages:
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
# Download the package details for the MongoDB packages:
sudo apt-get update
# Install MongoDB:
sudo apt-get install -y mongodb-org