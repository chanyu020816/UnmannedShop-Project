# Environment Setup

##  Requirement
1. Python >= 3.8
2. Pillow == 0.9.5 (Higher Version will cause error)
3. face_recognition 
4. ultralytics 
5. opencv-python
6. cvzone
7. google-cloud-bigquery >= 3.13.0
8. tkmacosx
9. numpy
10. google-api-python-client

## Pytorch & CUDA Setup on Jetson Orin Nano
```shell
# Create Virtual Environment
python3 -m venv env
source env/bin/activate

# Install Pytorch with CUDA (11.4) 
sudo apt-get -y update
sudo apt-get -y install autoconf bc build-essential g++-8 gcc-8 clang-8 lld-8 gettext-base gfortran-8 iputils-ping libbz2-dev libc++-dev libcgal-dev libffi-dev libfreetype6-dev libhdf5-dev libjpeg-dev liblzma-dev libncurses5-dev libncursesw5-dev libpng-dev libreadline-dev libssl-dev libsqlite3-dev libxml2-dev libxslt-dev locales moreutils openssl python-openssl rsync scons python3-pip libopenblas-dev;
export TORCH_INSTALL=https://developer.download.nvidia.cn/compute/redist/jp/v511/pytorch/torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64.whl
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64
python3 -m pip install --upgrade pip; python3 -m pip install aiohttp numpy=='1.19.4' scipy=='1.5.3' export "LD_LIBRARY_PATH=/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH"; python3 -m pip install --upgrade protobuf;# python3 -m pip install --no-cache $TORCH_INSTALL
pip install torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64.whl

# Install torchvision 0.15.1 compatible with Pytorch 2.0.0
git clone --branch release/0.15 https://github.com/pytorch/vision torchvision
export BUILD_VERSION=0.15.1
cd torchvision/
python3 setup.py install

# Here might has some bugs
# e.g RuntimeError: Python version >= 3.9 required.
# then we could not import torchvision even it is installed
pip install numpy
pip install urllib3
pip installcharest_normalizer

# rebuild torchvision
python3 setup.py install
sudo apt-get install libjpeg-dev libpng-dev

# Try import torchvision
# >>> import torchvision
# /home/chanyu/Desktop/Camera/torchvision/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: ''If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source?
# warn(
# /home/chanyu/Desktop/Camera/torchvision/torchvision/__init__.py:25: UserWarning: You are importing torchvision within its own root folder (/home/chanyu/Desktop/Camera/torchvision). This is not expected to work and may give errors. Please exit the torchvision project source and relaunch your python interpreter.
# warnings.warn(message.format(os.getcwd()))

# Reactivate Virtual Environment
deactivate
source ../env/bin/activate

# Now we can import torchvision and torch (with CUDA!!!)
```