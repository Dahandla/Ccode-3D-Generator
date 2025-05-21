🚀 Quick Setup Guide

 Installation
- See Release
+Please install PyTorch via the [official site](https://pytorch.org/). Then install the other requirements as described below:

> **Note:** For the most up-to-date and detailed setup instructions, including any additional dependencies or troubleshooting tips, please visit the [official Hunyuan3D 2.0 page](https://3d.hunyuan.tencent.com) or the [official GitHub repository](https://github.com/Tencent/Hunyuan3D-2).
>
1. Install Miniconda or Anaconda

If you don’t already have Conda, download and install Miniconda or Anaconda for your operating system.

2. Clone the Repository


Run
[git clone https://github.com/Dahandla/yourproject.git](https://github.com/Dahandla/Ccode-3D-Generator.git)

cd yourproject

3. Create the Conda Environment

Run
conda create -n Ccode3DGen_Hun


4. Activate the Environment
Run
conda activate Ccode3DGen_Hun


pip install -r requirements_v4.txt


This will create a new environment (e.g., Ccode3DGen_) with all required dependencies.

pip uninstall torch torchvision torchaudio -y

pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124

pip uninstall xformers
pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu124


pip uninstall segment-anything -y

pip install --no-cache-dir --force-reinstall segment-anything
pip install segment-anything

Reinstall segment_anything

pip install --force-reinstall git+https://github.com/facebookresearch/segment-anything.git


python.exe -m pip install --upgrade pip

# for texture
cd hy3dgen/texgen/custom_rasterizer
python setup.py install
pip install .

cd ../../..

cd hy3dgen/texgen/differentiable_renderer
python setup.py install




5. Run the Application

Run
python Ccode_3D.bat


6. Troubleshooting
If you encounter missing packages, try updating Conda:


Run
  conda update -n base -c defaults conda
If you have issues with PySide or DLLs, try:


Run
  conda install pyside6
That’s it! You’re ready to use the project.
If you have any issues, please check the README or open an issue on GitHub.

