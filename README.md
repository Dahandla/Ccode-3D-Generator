

 Ccode 3D Generator v1.4 - README

 Overview
Ccode 3D Generator is a powerful suite for generating, segmenting, and texturing 3D models from images, text prompts, and thumbnails. The latest version introduces an advanced image segmenter for extracting object parts, enabling part-based shape creation and seamless integration with the main 3D generation workflow.

![image](https://github.com/user-attachments/assets/c4d7a5ee-3486-4df5-b8a5-efbcf4fb8850)

 Ccode 3D Generator v1.4 -
 Features
- **3D Model Generation**: Convert images or text prompts into 3D models.
- **Image Part Segmentation (NEW)**: Use the integrated SAM-based segmenter to extract meaningful object parts from images, with options for LLM-guided filtering and part selection.
- **Part-Based Shape Creation (NEW)**: Select any segmented part and use it as the basis for 3D model generation or texturing.
- **Retexturing System**: Apply textures using text, images, or thumbnails.
- **Thumbnail-Based Texturing**: Select a previously generated texture from thumbnails.
- **HDRI Lighting Support**: Load environment maps for realistic rendering.
- **Customizable Parameters**: Adjust inference steps, octree resolution, guidance scale, and seed values.
- **Mesh Import & Export**: Load OBJ/GLB files, apply textures, and export in various formats.
- **Automated Caching & File Management**: Organizes generated models and textures.
- **Unified Theme Selector**: Choose between Light, Dark, and Blue themes across all GUIs.

 Installation
- See Release
+Please install PyTorch via the [official site](https://pytorch.org/). Then install the other requirements as described below:
+

pip install -r requirements.txt

pip install -e .

for texture
cd hy3dgen/texgen/custom_rasterizer

python3 setup.py install

cd ../../..

cd hy3dgen/texgen/differentiable_renderer

python3 setup.py install


> **Note:** For the most up-to-date and detailed setup instructions, including any additional dependencies or troubleshooting tips, please visit the [official Hunyuan3D 2.0 page](https://3d.hunyuan.tencent.com) or the [official GitHub repository](https://github.com/Tencent/Hunyuan3D-2).

 How to Use
 1. Generating a 3D Model
- Select an **image** or enter a **text prompt**.
- Adjust parameters like inference steps and resolution.
- Click **"Generate Shape"** for a 3D model or **"Generate Shape and Texture"** to apply a texture.

 2. Segmenting an Image into Parts (NEW)
- Click **"Start SAM Segmenter"** in the main app directly.
- Load an input image and (optionally) set the output directory.
- Adjust segmentation parameters or use the LLM filter for meaningful parts.
- Click **"Start Automatic Segmentation"** to generate parts:
  - View the original, full-object ("fullbody"), and individual part images.
  - Navigate through parts and preview them interactively.
  - Click **"Send to Main App"** to use a selected part in the main 3D generator.

 3. Retexturing a Mesh
- Load an existing 3D model.
- Use either:
  - **Text Input**: Describe the texture in words.
  - **Image Input**: Upload a texture image.
  - **Thumbnail Selection**: Choose from previously generated textures.
- Click **"Retexture Mesh"** to apply the texture.

 4. Saving and Exporting
- Click **"Save Mesh"** to export in `.glb` or `.obj` format.
- Textures are automatically saved alongside the model.

 Special Features
 Image Part Segmenter & Shape Creation (NEW)
- **Automatic Mask Generator**: Segment images into meaningful parts using the Segment Anything Model (SAM).
- **LLM Integration**: Optionally use a language model to filter and name parts for more semantic segmentation.
- **Interactive Part Selection**: Preview, navigate, and select any part for further 3D processing.
- **Full Object Mask ("Fullbody")**: Instantly create a mask of the entire object (union of all parts) for whole-object workflows.
- **Parts Sheet**: Generate a grid overview of all segmented parts for easy inspection.
- **Seamless Integration**: Send any part image directly to the main 3D generator for shape or texture creation.

 Retexturing & Texture Inputs
- The script allows nuanced texture application from multiple sources:
  - **Text-Based**: AI generates a texture from a textual description.
  - **Image-Based**: Users can upload an image to be used as texture.
  - **Thumbnail-Based**: Quick reapplication of previous textures.

 Texturing Workflow
1. If using **text input**, it generates an image first and then applies it.
2. If using **an uploaded image**, it directly applies the texture.
3. If using a **thumbnail**, it either re-applies a stored mesh or regenerates the texture.

 Advanced Options
- **Guidance Scale**: Adjusts how strongly the model follows the text prompt.
- **Octree Resolution**: Determines the model's detail level.
- **Seed Value**: Ensures repeatable generations.
- **HDRI Support**: Load HDRI images for realistic lighting.
- **Theme Selector**: Choose Light, Dark, or Blue theme for all GUIs.
- **Collapsible Parameter Sections**: Hide advanced controls for a cleaner UI.
- **Tooltips**: Hover over any parameter for detailed help.

 Troubleshooting
- **Mesh doesn't appear?** Try reloading the view.
- **Texture not applying?** Ensure the texture file exists and is correctly referenced.
- **Performance issues?** Reduce the inference steps or octree resolution.
- **SAM/Segmenter not launching?** Ensure all dependencies are installed and the correct Python environment is used.

 License & Legal Notice
This project utilizes **Tencent Hunyuan 3D 2.0**, which is governed by the **Tencent Hunyuan 3D 2.0 Community License Agreement**. 

**Important Notes:**
- This software **CANNOT be used in the European Union, United Kingdom, or South Korea** due to Tencent's licensing restrictions.
- Redistribution is allowed **only if the original license and notices are included**.
- Users must **not use this model for prohibited purposes** (e.g., law enforcement, medical applications, harmful AI usage).
- If the software reaches **over 1 million users, a commercial license from Tencent is required**.

For full details, see the [LICENSE](LICENSE.txt) and [NOTICE](NOTICE.txt) files.

 Donations
If you find this project useful and would like to support further development, you can donate via:
- GitHub: [github.com/dahandla](https://github.com/dahandla)
- YouTube: [youtube.com/@Dahandla](https://www.youtube.com/@Dahandla)
- Donations: [PayPal](https://www.paypal.com/paypalme/AndreDickinson?locale=en_US)

Your contributions help keep this project alive! ❤️

 Contact & Support
- E-mail saraintelai@gmail.com

 Acknowledgments
- **Tencent Hunyuan 3D 2.0** - For providing the core 3D model generation technology.
- **Stability AI (Stable Diffusion)** - If used in generating textures.
- **Meta AI (SAM)** - For the Segment Anything Model powering the part segmenter.

## Ollama Integration for Image Description

[Ccode 3D Generator](https://ollama.com/) leverages Ollama, a local large language model (LLM) runner, to enhance the workflow with AI-generated image descriptions. Ollama enables you to run advanced LLMs (such as Llama 3, Qwen, DeepSeek, and others) directly on your machine, ensuring privacy and fast inference.

### How Ollama is Used
- **Image Description Generation:** When the "Use Image Description" option is enabled in the app, Ollama is used to generate a human-readable description of the input image. This description is then automatically populated into the text prompt field, making it easier to generate 3D models from images.
- **How it works in the script:** The script (see `Ccode3DGen_Hun.pyx`) uses the `ollama` Python package to send the image to a local Ollama server, which returns a description using a vision-capable LLM (e.g., `moondream` or `llava-llama3`).

### How to Set Up Ollama
1. **Download and Install Ollama:**  
   Visit [https://ollama.com/](https://ollama.com/) and follow the instructions for your operating system.

2. **Run an LLM Model:**  
   After installation, start Ollama and load a model (e.g., Moondream or LLaVA) using the command:
   ```
   ollama run moondream
   ```
   or
   ```
   ollama run llava-llama3
   ```
   (You can use any vision-capable model supported by Ollama.)

3. **Enable Image Description in the App:**  
   In the app, check the "Use Image Description" box. When you load an image, the app will automatically generate a description using Ollama and fill it into the text prompt field.

4. **Privacy & Performance:**  
   All LLM inference is performed locally; no data is sent to external servers.

For more information about Ollama, visit [https://ollama.com/](https://ollama.com/).

---
**Version:** 1.4  
**Author:** Andre Dickinson  
**Date:** 2025-01-30  

🚀 *Happy Texturing and Segmenting!*





