# 🌊 Bayes Decision Rule for River/Non-River Segmentation 🌊

## Overview
This project demonstrates a scratch implementation of Bayes Decision Rule to segment river and non-river areas in images using the Naive Bayes classification algorithm.

## 🚀 Getting Started

### 1. Choose an Image
- Select any `.gif` file you wish to segment.
- Update the `"img_filename"` variable in `annote_image_points.py` with the chosen `.gif` file.

### 2. Annotate Points
- Execute `annote_image_points.py`.
- Click 150 points on the non-river areas and 50 points on the river areas within the image.
- Once the annotation is complete, a new `.csv` file will be generated, such as `annotated_points_band4_np_50.csv` and `annotated_points_band4_np_150.csv`.

### 3. Run the Notebook
- Open the provided `.ipynb` notebook file.
- Run the cells to process the annotated points and perform segmentation.

## 🎉 Results
- The result will be a segmented image highlighting river and non-river regions, classified using the Naive Bayes algorithm.
