🚀 Quick Setup Guide

1. Install Miniconda or Anaconda

If you don’t already have Conda, download and install Miniconda or Anaconda for your operating system.

2. Clone the Repository


Run
https://github.com/Dahandla/Ccode-3D-Generator.git


cd yourproject

3. Create the Conda Environment

Run
conda env create -f environment.yml

This will create a new environment (e.g., Ccode3DGen_) with all required dependencies.

4. Activate the Environment


Run
conda activate Ccode3DGen_
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
