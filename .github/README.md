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

 # Applying SMILE on DeepMind's Gemini  

🚀 This repository explores the application of **SMILE (Statistical Model-Agnostic Interpretability for Local Explanation)** on **Gemini**, DeepMind’s newly developed model. Our approach enhances interpretability in instruction-based image editing models, allowing for a deeper understanding of how textual prompts influence AI-generated transformations.  

🔗 [View the Kaggle Notebook](https://www.kaggle.com/code/zeinabdehghani/explain-gemini-image-editing-with-smile)  
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


## 🔥 Generating Heatmaps

The process of generating heatmaps is explained in detail in the following flowchart:

🔗 **[View Flowchart](https://github.com/Sara068/Explain-Instruction-based-Image-Editing-models/blob/main/docs/Figures/flow.png)**


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

```bibtex
@article{dehghani2024mapping,
  title={Mapping the Mind of an Instruction-based Image Editing using SMILE},
  author={Dehghani, Zeinab and Aslansefat, Koorosh and Khan, Adil and Rivera, Ad{\'\i}n Ram{\'\i}rez and George, Franky and Khalid, Muhammad},
  journal={arXiv preprint arXiv:2412.16277},
  year={2024}
}



