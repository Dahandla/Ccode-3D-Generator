🚀 Quick Setup Guide

 Installation
- See Release
+Please install PyTorch via the [official site](https://pytorch.org/). Then install the other requirements as described below:

> **Note:** For the most up-to-date and detailed setup instructions, including any additional dependencies or troubleshooting tips, please visit the [official Hunyuan3D 2.0 page](https://3d.hunyuan.tencent.com) or the [official GitHub repository](https://github.com/Tencent/Hunyuan3D-2).
>
> 
pip install -r requirements.txt

pip install -e .

for texture
cd hy3dgen/texgen/custom_rasterizer

python3 setup.py install

cd ../../..

cd hy3dgen/texgen/differentiable_renderer

python3 setup.py install



1. Install Miniconda or Anaconda

If you don’t already have Conda, download and install Miniconda or Anaconda for your operating system.

2. Clone the Repository


Run
git clone https://github.com/Dahandla/yourproject.git

cd yourproject

3. Create the Conda Environment

Run
conda create -n Ccode3DGen_


4. Activate the Environment
Run
conda activate Ccode3DGen_


pip install -r requirements_v4.txt


This will create a new environment (e.g., Ccode3DGen_) with all required dependencies.

pip uninstall torch torchvision torchaudio -y
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121


Reinstall segment_anything

pip install --force-reinstall git+https://github.com/facebookresearch/segment-anything.git

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
