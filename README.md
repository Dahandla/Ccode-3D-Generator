# Ccode 3D Generator v1.4 - README

## Overview
Ccode 3D Generator is a powerful suite for generating, segmenting, and texturing 3D models from images, text prompts, and thumbnails. The latest version introduces an advanced image segmenter for extracting object parts, enabling part-based shape creation and seamless integration with the main 3D generation workflow.

## Features
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

## Installation
See Release

## How to Use
### 1. Generating a 3D Model
- Select an **image** or enter a **text prompt**.
- Adjust parameters like inference steps and resolution.
- Click **"Generate Shape"** for a 3D model or **"Generate Shape and Texture"** to apply a texture.

### 2. Segmenting an Image into Parts (NEW)
- Click **"Start SAM Segmenter"** in the main app directly.
- Load an input image and (optionally) set the output directory.
- Adjust segmentation parameters or use the LLM filter for meaningful parts.
- Click **"Start Automatic Segmentation"** to generate parts:
  - View the original, full-object ("fullbody"), and individual part images.
  - Navigate through parts and preview them interactively.
  - Click **"Send to Main App"** to use a selected part in the main 3D generator.

### 3. Retexturing a Mesh
- Load an existing 3D model.
- Use either:
  - **Text Input**: Describe the texture in words.
  - **Image Input**: Upload a texture image.
  - **Thumbnail Selection**: Choose from previously generated textures.
- Click **"Retexture Mesh"** to apply the texture.

### 4. Saving and Exporting
- Click **"Save Mesh"** to export in `.glb` or `.obj` format.
- Textures are automatically saved alongside the model.

## Special Features
### Image Part Segmenter & Shape Creation (NEW)
- **Automatic Mask Generator**: Segment images into meaningful parts using the Segment Anything Model (SAM).
- **LLM Integration**: Optionally use a language model to filter and name parts for more semantic segmentation.
- **Interactive Part Selection**: Preview, navigate, and select any part for further 3D processing.
- **Full Object Mask ("Fullboy")**: Instantly create a mask of the entire object (union of all parts) for whole-object workflows.
- **Parts Sheet**: Generate a grid overview of all segmented parts for easy inspection.
- **Seamless Integration**: Send any part image directly to the main 3D generator for shape or texture creation.

### Retexturing & Texture Inputs
- The script allows nuanced texture application from multiple sources:
  - **Text-Based**: AI generates a texture from a textual description.
  - **Image-Based**: Users can upload an image to be used as texture.
  - **Thumbnail-Based**: Quick reapplication of previous textures.

### Texturing Workflow
1. If using **text input**, it generates an image first and then applies it.
2. If using **an uploaded image**, it directly applies the texture.
3. If using a **thumbnail**, it either re-applies a stored mesh or regenerates the texture.

## Advanced Options
- **Guidance Scale**: Adjusts how strongly the model follows the text prompt.
- **Octree Resolution**: Determines the model's detail level.
- **Seed Value**: Ensures repeatable generations.
- **HDRI Support**: Load HDRI images for realistic lighting.
- **Theme Selector**: Choose Light, Dark, or Blue theme for all GUIs.
- **Collapsible Parameter Sections**: Hide advanced controls for a cleaner UI.
- **Tooltips**: Hover over any parameter for detailed help.

## Troubleshooting
- **Mesh doesn't appear?** Try reloading the view.
- **Texture not applying?** Ensure the texture file exists and is correctly referenced.
- **Performance issues?** Reduce the inference steps or octree resolution.
- **SAM/Segmenter not launching?** Ensure all dependencies are installed and the correct Python environment is used.

## License & Legal Notice
This project utilizes **Tencent Hunyuan 3D 2.0**, which is governed by the **Tencent Hunyuan 3D 2.0 Community License Agreement**. 

**Important Notes:**
- This software **CANNOT be used in the European Union, United Kingdom, or South Korea** due to Tencent's licensing restrictions.
- Redistribution is allowed **only if the original license and notices are included**.
- Users must **not use this model for prohibited purposes** (e.g., law enforcement, medical applications, harmful AI usage).
- If the software reaches **over 1 million users, a commercial license from Tencent is required**.

For full details, see the [LICENSE](LICENSE.txt) and [NOTICE](NOTICE.txt) files.

## Donations
If you find this project useful and would like to support further development, you can donate via:
- GitHub: [github.com/dahandla](https://github.com/dahandla)
- YouTube: [youtube.com/@Dahandla](https://www.youtube.com/@Dahandla)
- Donations: [PayPal](https://www.paypal.com/paypalme/AndreDickinson?locale=en_US)

Your contributions help keep this project alive! ❤️

## Contact & Support
- E-mail saraintelai@gmail.com

## Acknowledgments
- **Tencent Hunyuan 3D 2.0** - For providing the core 3D model generation technology.
- **Stability AI (Stable Diffusion)** - If used in generating textures.
- **Meta AI (SAM)** - For the Segment Anything Model powering the part segmenter.

---
**Version:** 1.4  
**Author:** Andre Dickinson  
**Date:** 2025-4-30  

🚀 *Happy Texturing and Segmenting!*

