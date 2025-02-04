## Mapping the Mind of an Instruction-based Image Editing using <a href = "https://github.com/Dependable-Intelligent-Systems-Lab/xwhy"><b>SMILE</b></a>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E-HAiu2tORA2AgT1OkqAxlLzEvSJ5kY8)

[Zeinab Dehghani](https://github.com/Sara068), [Koorosh Aslansefat](https://github.com/koo-ec), [Adil Khan], [Adín Ramírez Rivera], [Franky George], [Muhammad Khalid].



## Project Description
<p align="justify">The lack of interpretability in diffusion-based image generation models remains a significant barrier to transparency and user trust, despite recent advancements in generating high-quality images from textual descriptions. To address this challenge, we propose SMILE (Statistical Model-agnostic Interpretability with Local Explanations), a novel, model-agnostic approach designed to provide localized explanations and visual heatmaps that clarify how specific textual elements influence image generation. Applied across leading models—including Pix2Pix, DALL-E, Learnable Region, and Diffusers-Inpaint—our method demonstrates substantial improvements in interpretability and reliability, as evidenced by rigorous evaluations on stability, accuracy, fidelity, and consistency metrics. These findings underscore the potential of model-agnostic interpretability solutions, paving the way for transparent and trustworthy AI in high-stakes applications like healthcare and autonomous driving, while inviting further exploration into the role of interpretability in advancing reliable image editing models.</p>
 <img src="https://github.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE/blob/main/docs/Figures/diff prompt (1).png" alt="example">

## Video Explaining the Approach

<p align="center">
  <a href="https://www.youtube.com/watch?v=0QTf2qasrgM">
    <img src="https://img.youtube.com/vi/0QTf2qasrgM/maxresdefault.jpg" 
         alt="Mapping the Mind of Instruction-based Image Editing using SMILE" 
         width="800">
  </a>
</p>

 
## Method Overview

 <img src="https://github.com/Sara068/Explain-Instruction-based-Image-Editing-models/blob/main/docs/Figures/flow.png" alt="Proposed Flowchart">

 ## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Generating Heatmaps](#generating-heatmaps)
  - [Evaluating Models](#evaluating-models)
- [Citation](#citation)

## Installation

## 🚀 Installation Guide

Follow these steps to set up and run the project.

### 1️⃣ Clone the Repository
To clone the repository to your local machine, use the following command:
```bash
git clone https://github.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE.git
cd Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Running the Script Locally
Once dependencies are installed, you can run the main script using the following command:
```bash
python SMILE_Image_Editing.py
```
📜 Citation

If you use this work, please cite the following paper:
@article{dehghani2024mapping,
  title={Mapping the Mind of an Instruction-based Image Editing using SMILE},
  author={Dehghani, Zeinab and Aslansefat, Koorosh and Khan, Adil and Rivera, Ad{\'\i}n Ram{\'\i}rez and George, Franky and Khalid, Muhammad},
  journal={arXiv preprint arXiv:2412.16277},
  year={2024}
}



