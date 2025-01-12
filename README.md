# Creative Scoring Predictions

This repository contains a Jupyter Notebook (`creative_scoring_predictions.ipynb`) that analyzes creative assets' performance and predicts their effectiveness. The project utilizes Python's data analysis and machine learning libraries for preprocessing, analysis, and evaluation.

## Features

### Workflow Steps:
1. **Importing Data**:
   - Load the dataset (`creatives_c.csv`) for analysis using Pandas.

2. **Exploratory Data Analysis (EDA)**:
   - Explore the dataset for trends, missing values, and basic statistics.
   - Visualize key insights using Matplotlib and Seaborn.

3. **Renaming and Cleaning Columns**:
   - Rename columns for better readability and consistency.
   - Remove irrelevant or redundant columns.

4. **Classification (Ad Evaluation)**:
   - Evaluate whether an ad is "Good" or "Bad" based on statistical methods such as mean and standard deviation of key metrics.

5. **Encoding**:
   - Encode categorical variables to prepare data for modeling.

6. **Data Splitting**:
   - Split the dataset into training and testing sets for model evaluation.

7. **Prediction**:
   - Use machine learning models to predict the effectiveness of ads.

8. **Classification and Model Evaluation**:
   - Evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score.
   - Generate classification reports and confusion matrices.

## Requirements

Ensure you have the following Python packages installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `sklearn`

Install the required packages using:
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn