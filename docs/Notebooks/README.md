# t-SNE Plot in Notebooks

## Plot Description

In this project, the t-SNE technique was used to reduce the dimensionality of image embeddings. The plot below visualizes the 2D distribution of embeddings, showing clear clustering of data points based on different prompt keywords. These clusters highlight the separation between features corresponding to specific textual prompts and those with perturbed or non-specific prompts.

---

### Image Link

The t-SNE plot is saved in the following location:

[`docs/Figures/plot_tsne (2).jpg`](../Figures/plot_tsne%20(2).jpg)

---

### Code to Generate the t-SNE Plot

The following code snippet was used to display the t-SNE plot in a Jupyter Notebook:

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display the image
img = mpimg.imread('../Figures/plot_tsne (2).jpg')  # Path to the image
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')  # Hide axes for a cleaner visualization
plt.title("2D t-SNE visualization of image embeddings", fontsize=14)
plt.show()
