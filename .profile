# install advanced dependencies
wget https://download.pytorch.org/whl/cpu/torch-1.11.0%2Bcpu-cp39-cp39-linux_x86_64.whl
pip3 install torch-1.11.0+cpu-cp39-cp39-linux_x86_64.whl
rm -f torch-1.11.0+cpu-cp39-cp39-linux_x86_64.whl

wget https://download.pytorch.org/whl/cpu/torchvision-0.12.0%2Bcpu-cp39-cp39-linux_x86_64.whl
pip3 install torchvision-0.12.+cpu-cp39-cp39-linux_x86_64.whl
rm -f torchvision-0.12.+cpu-cp39-cp39-linux_x86_64.whl