# Terra Store Product Recommendation System

## Overview
This project develops an AI-powered web application to predict the next product a customer is likely to purchase based on historical data.

## Features
- Predicts top N recommended products for a customer.
- User-friendly web interface for marketing teams.
- Built with Python, Flask, TensorFlow, and basic HTML/JavaScript.

## Setup and Installation
1. Clone the repository.
    ```bash
    git clone https://github.com/yourusername/terra-store-recommendation.git
    ```
2. Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```
3. Run the data preprocessing script.
    ```bash
    python src/data_preprocessing.ipynb
    ```
3. Run the Streamlit App
   ```streamlit run appv2.py
    This command will launch the app, and you can access it by visiting the provided URL in your web browser.

## Usage
1. Enter a customer ID.
2. Click "Get Recommendations".
3. View the recommended products.

## Data
- `customer_interactions.csv`: Contains customer interaction data like page views and time spent.
- `purchase_history.csv`: Contains records of customer purchases.
- `product_details.csv`: Provides details about each product.

## Model
- SVD - Singular Value Decomposition
- KNN Basic models based on their evaluation metrics

## Contact
For any inquiries, please contact [rachdiaaan@gmail.com].
