# battery-date-time-app

# READ FIRST:
- right click on the app on the taskbar
- more
- keep above others

#### More info for date, time format:
- https://devhints.io/datetime

#### Originally tested on Manjaro 23 KDE Plasma 5.27.6

### How to run?

# Arch-based distros (e.g., Manjaro, Arch Linux)

sudo pacman -S python
sudo pacman -S qt5-base
sudo pacman -S python-psutil

# Debian-based distros (e.g., Ubuntu, Linux Mint)

### Install Python and pip (python3 is recommended)

sudo apt-get update
sudo apt-get install python3 python3-pip
sudo apt-get install python3-pyqt5
sudo apt-get install python3-psutil

# Fedora-based distros (e.g., Fedora, RHEL)

sudo dnf install python3 python3-pip
sudo dnf install python3-qt5
sudo dnf install python3-psutil

python3 <path_to_file>/bdt.py
