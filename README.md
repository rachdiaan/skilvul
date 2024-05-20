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
    python src/data_preprocessing.py
    ```
4. Train the model.
    ```bash
    python src/model_training.py
    ```
5. Run the Flask app.
    ```bash
    python src/app.py
    ```
6. Access the web app at `http://127.0.0.1:5000`.

## Usage
1. Enter a customer ID.
2. Click "Get Recommendations".
3. View the recommended products.

## Data
- `customer_interactions.csv`: Contains customer interaction data like page views and time spent.
- `purchase_history.csv`: Contains records of customer purchases.
- `product_details.csv`: Provides details about each product.

## Model
- Neural Collaborative Filtering (NCF) model using TensorFlow.

## Contact
For any inquiries, please contact [rachdiaaan@gmail.com].
