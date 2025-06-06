🚀 Quick Setup Guide


![image](https://github.com/Dahandla/Ccode-3D-Generator/blob/23849830b42db8ea3b9d9f046362c199dab8ddc9/resources/Ccode3DGenHalfScreen.png)


 Installation
- See Release
+Please install PyTorch via the [official site](https://pytorch.org/). Then install the other requirements as described below:

> **Note:** For the most up-to-date and detailed setup instructions, including any additional dependencies or troubleshooting tips, please visit the [official Hunyuan3D 2.0 page](https://3d.hunyuan.tencent.com) or the [official GitHub repository](https://github.com/Tencent/Hunyuan3D-2).
>
## Prerequisites
- Windows 10/11
- NVIDIA GPU with CUDA support (recommended)
- Git
- Miniconda or Anaconda

- 
## ⚠️ Important Note About Model Files
On first run, the application will automatically download the required model files. This process:
- May take 15-30 minutes, depending on your internet connection
- Downloads will be cached locally for future use
- Ensure you have enough space on your hard drive and  a stable internet connection for the initial setup

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/Dahandla/Ccode-3D-Generator.git
cd Ccode-3D-Generator
```

### 2. Set Up Conda Environment
```bash
# Create new environment
conda create -n Ccode3DGen_Hun_v2 python=3.10
conda activate Ccode3DGen_Hun_v2
```

### 3. Install Dependencies


pip install -r requirements_v4.txt


#### 3.1 Install PyTorch
```bash
# Remove existing PyTorch installation if any
pip uninstall torch torchvision torchaudio -y

# Install PyTorch with CUDA 12.4 support
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
```

#### 3.2 Install Additional Requirements
```bash
# Install xformers for better performance
pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu124

# Install numpy
pip install --upgrade numpy==1.24.4

# Install segment-anything
pip uninstall segment-anything -y
pip install git+https://github.com/facebookresearch/segment-anything.git
```

#### 3.3 Install Texture Generation Components
```bash
# Install custom rasterizer
cd hy3dgen/texgen/custom_rasterizer
python setup.py install
cd ../../..

# Install differentiable renderer
cd hy3dgen/texgen/differentiable_renderer
python setup.py install
cd ../../..
```

### 4. Run the Application
```bash
python run_app.py
```

## Troubleshooting

### Common Issues

1. **Missing Packages**

2. You should be able to ignore the 'triton' error safely. Do not try to install it, I think it is just for Linux, not Windows, and if there is a Windows version, it would cause an issue with the code.
   ```bash
   conda update -n base -c defaults conda
   ```

3. **PySide/DLL Issues**
   ```bash
   conda install pyside6
   ```

4. **CUDA Compatibility**
   - Ensure your NVIDIA drivers are up to date
   - Verify CUDA compatibility with your GPU

## Support

For additional help:
- Check the [README.md](README.md) for detailed documentation
- Open an issue on [GitHub](https://github.com/Dahandla/Ccode-3D-Generator/issues)
- Contact: saraintelai@gmail.com

## System Requirements
- NVIDIA GPU with 8GB+ VRAM (recommended)
- 16GB+ RAM
- 20GB+ free disk space
- Windows 10/11 64-bit

---
*Created by Andre Dickinson | Last Updated: 2025-01-30*
