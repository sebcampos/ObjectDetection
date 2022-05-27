
# Set up
- `sudo raspi-config` then interfaces then camera then enable

# Tensorflow tutorial
- pip install tensorflow-aarch64

# Camera related commands
- `raspistill -t <time_in_milliseconds> -o <filename>.jpg` <- takes an image
- `raspistill --help` <- help menu
- `raspivid -o -t <time_in_milliseconds> <filename>.h264` <- takes a video need to use .h264 extention
