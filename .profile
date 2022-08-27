# update system
apt-get update

# install basic dependencies, assuming python3 is installed
apt-get install htop wget python3-pip

# install advanced dependencies
pip3 install numpy==1.21

wget https://download.pytorch.org/whl/cpu/torch-1.11.0%2Bcpu-cp39-cp39-linux_x86_64.whl
pip3 install torch-1.11.0+cpu-cp39-cp39-linux_x86_64.whl
rm -f torch-1.11.0+cpu-cp39-cp39-linux_x86_64.whl

wget https://download.pytorch.org/whl/cpu/torchvision-0.12.0%2Bcpu-cp39-cp39-linux_x86_64.whl
pip3 install torchvision-0.12.+cpu-cp39-cp39-linux_x86_64.whl
rm -f torchvision-0.12.+cpu-cp39-cp39-linux_x86_64.whl