## Mapping the Mind of an Instruction-based Image Editing using <a href = "https://github.com/Dependable-Intelligent-Systems-Lab/xwhy"><b>SMILE</b></a>
[![Open In Colab (Original)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E-HAiu2tORA2AgT1OkqAxlLzEvSJ5kY8)
[![Open In Colab (Latest Notebook)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HygOW6XsKgXdC6FhJhh2Vi6a5lnitMzB?usp=sharing)

[Zeinab Dehghani](https://github.com/Sara068), [Koorosh Aslansefat](https://github.com/koo-ec), [Hamed Daneshvar](http://github.com/HamedDaneshvar), [Adil Khan], [Adín Ramírez Rivera], [Franky George], [Muhammad Khalid].



## Project Description
<p align="justify">The lack of interpretability in diffusion-based image generation models remains a significant barrier to transparency and user trust, despite recent advancements in generating high-quality images from textual descriptions. To address this challenge, we propose SMILE (Statistical Model-agnostic Interpretability with Local Explanations), a novel, model-agnostic approach designed to provide localized explanations and visual heatmaps that clarify how specific textual elements influence image generation. Applied across leading models—including Pix2Pix, DALL-E, Learnable Region, and Diffusers-Inpaint—our method demonstrates substantial improvements in interpretability and reliability, as evidenced by rigorous evaluations on stability, accuracy, fidelity, and consistency metrics. These findings underscore the potential of model-agnostic interpretability solutions, paving the way for transparent and trustworthy AI in high-stakes applications like healthcare and autonomous driving, while inviting further exploration into the role of interpretability in advancing reliable image editing models.</p>

<img src="https://raw.githubusercontent.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE/refs/heads/main/docs/Figures/diff%20prompt%20(1).png" alt="example">

### Public Kaggle Notebooks
- [IE-SMILE img2img-turbo low-level-editing on Kaggle](https://www.kaggle.com/code/hameddaneshvar/i2e-bench-img2img-turbo-low-level-editing)
- [IE-SMILE img2img-turbo high-level-editing on Kaggle](https://www.kaggle.com/code/hameddaneshvar/i2e-bench-img2img-turbo-high-level-editing)
- [IE-SMILE Gemini on Kaggle](https://www.kaggle.com/code/kooaslansefat/i2e-bench-ie-smile-gemini)
- [IE-SMILE SeeDream on Kaggle](https://www.kaggle.com/code/kooaslansefat/i2e-bench-ie-smile-seedream)
- [Attribute AUC Notebook on Kaggle](https://www.kaggle.com/code/hameddaneshvar/i2e-bench-auc/)
- [Stability Test Nootbook on Kaggle](https://www.kaggle.com/code/hameddaneshvar/i2e-bench-stability)

## Video Explaining the Approach

<p align="center">
  <a href="https://www.youtube.com/watch?v=0QTf2qasrgM">
    <img src="https://img.youtube.com/vi/0QTf2qasrgM/maxresdefault.jpg"
         alt="Mapping the Mind of Instruction-based Image Editing using SMILE"
         width="800">
  </a>
</p>

# Applying SMILE on DeepMind's Gemini

🚀 This repository explores the application of **SMILE (Statistical Model-Agnostic Interpretability for Local Explanation)** on **Gemini**, DeepMind’s newly developed model. Our approach enhances interpretability in instruction-based image editing models, allowing for a deeper understanding of how textual prompts influence AI-generated transformations.
🔗 [View the Kaggle Notebook](https://www.kaggle.com/code/zeinabdehghani/explain-gemini-image-editing-with-smile)

## Method Overview

<img src="https://raw.githubusercontent.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE/refs/heads/main/docs/Figures/flow.png" alt="Proposed Flowchart">

## Table of Contents
- [Installation](#installation)
  - [Recommended: Using uv (Latest and Preferred Method)](#recommended-using-uv-latest-and-preferred-method)
  - [Legacy Method: Using pip](#legacy-method-using-pip)
- [Usage](#usage)
  - [Running the Latest Code](#running-the-latest-code)
  - [Running the Original Script](#running-the-original-script)
  - [Generating Heatmaps](#generating-heatmaps)
  - [Evaluating Models](#evaluating-models)
- [Citation](#citation)

## Installation

## 🚀 Installation Guide

Follow these steps to set up and run the project.

### Latest Changes
- Now we support **Gemini**, **SeeDream**, and **OpenAI** as commercial models too.

### Recommended: Using uv (Latest and Preferred Method)
**uv** is the fastest and most reliable way to manage dependencies for this project. It automatically handles virtual environments and uses the `uv.lock` file for reproducible installations.

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE.git
cd Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE
```

2️⃣ **Install Dependencies with uv**
```bash
uv sync
```
This command will:
- Create a virtual environment (`.venv`) if needed
- Install all dependencies exactly as specified in `uv.lock`
- Ensure full reproducibility across machines

To activate the environment manually (optional, as `uv run` handles it automatically):
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Legacy Method: Using pip
If you prefer the traditional approach:

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE.git
cd Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE
```

2️⃣ **Create and Activate a Virtual Environment**
```bash
python -m venv env
source env/bin/activate    # macOS/Linux
env\Scripts\activate       # Windows
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

## Usage

### Running the Latest Code
Recommended: Use `uv run` for automatic environment management.

- Run the notebook:
  ```bash
  uv run jupyter notebook IIE_SMILE/SMILE_for_Instruction_based_Image_Editing.ipynb
  ```
- Or run the Python script:
  ```bash
  uv run IIE_SMILE/SMILE_for_Instruction_based_Image_Editing.py
  ```

### Running the Original Script
```bash
python SMILE_Image_Editing.py
```


## 🔥 Generating Heatmaps

The process of generating heatmaps is explained in detail in the following flowchart:

🔗 **[View Flowchart](https://github.com/Sara068/Mapping-the-Mind-of-an-Instruction-based-Image-Editing-using-SMILE/blob/main/docs/Figures/flowchat_.png)**


## 📊 Evaluation of Model Performance
To assess the performance of the explainability framework, we use the following evaluation metrics:
1️⃣ **Accuracy**
   - Measures how well model explanations align with ground truth.
   - Uses **Attention AUROC, Attention F1 Score (ATT F1), and Attention Accuracy (ATT ACC)** to compare attribution scores with expected word importance.
2️⃣ **Stability**
   - Ensures that minor variations in input (e.g., punctuation changes) do not cause drastic changes in attribution.
   - Measured using the **Jaccard Index** to quantify consistency across minor perturbations.
3️⃣ **Consistency**
   - Evaluates whether the model produces stable explanations for the same input across multiple runs.
   - Measured using **variance and standard deviation** of explanation scores.
4️⃣ **Fidelity**
   - Assesses how well the explainability model aligns with the black-box model it explains.
   - Metrics include **Weighted Mean Squared Error (WMSE), R² coefficient, Mean Absolute Error (MAE), and Mean L1 & L2 losses**.

These metrics ensure that our explainability method is reliable, interpretable, and stable, making **SMILE** a robust framework for understanding instruction-based image editing models.

## 📜 Citation

If you use this work, please cite the following paper:

```bibtex:disable-run
@article{dehghani2024mapping,
  title={Mapping the Mind of an Instruction-based Image Editing using SMILE},
  author={Dehghani, Zeinab and Aslansefat, Koorosh and Khan, Adil and Rivera, Ad{\'\i}n Ram{\'\i}rez and George, Franky and Khalid, Muhammad},
  journal={arXiv preprint arXiv:2412.16277},
  year={2024}
}
```
