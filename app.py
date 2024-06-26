import streamlit as st
import pandas as pd
from surprise.dump import load
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import Dataset, Reader
import requests
from joblib import dump, load
import plotly.express as px

# Set the page title and favicon
st.set_page_config(page_title="E-commerce Recommender App", page_icon="🛍️")

# Load the dataset
df = pd.read_csv('merged_data.csv')

# Function to download and load the SVD model
def load_svd_model(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("svd_model.joblib", "wb") as f:
            f.write(response.content)
        return load("svd_model.joblib")
    else:
        return None

# Load the SVD model from the file
svd_model_url = 'https://github.com/rachdiaan/skilvul/raw/main/svd_model.joblib'
loaded_svd_model = load_svd_model(svd_model_url)

# Check if the model was loaded successfully
if loaded_svd_model is not None:
    st.success("SVD Model loaded successfully")
    # Verify the loaded model
    # st.write(loaded_svd_model)
else:
    st.error("Failed to load the SVD model. Please check the URL.")

def get_top_n_recommendations(model, user_id, n=5):
    # Check if the user ID is in the dataset
    if user_id not in df['customer_id'].unique():
        st.warning(f"No data available for customer with ID {user_id}. Please check if the customer has provided ratings.")
        return []

    # Get a list of all product IDs
    all_products = df['product_id'].unique()

    # Get the products the user has already purchased
    purchased_products = df[df['customer_id'] == user_id]['product_id'].tolist()

    # Remove the purchased products from the list
    to_predict = [prod for prod in all_products if prod not in purchased_products]

    # Check if there are items to predict
    if not to_predict:
        st.warning(f"No products available for recommendation for customer with ID {user_id}.")
        return []

    # Predict ratings for products that the user has not purchased
    predictions = [model.predict(user_id, prod) for prod in to_predict]

    # Sort predictions by estimated rating
    predictions.sort(key=lambda x: x.est, reverse=True)

    # Display the top N recommended products
    top_n_recommendations = predictions[:n]
    if not top_n_recommendations:
        st.warning(f"No recommendations available for customer with ID {user_id}. Please check if the customer has provided ratings.")
        return []
    else:
        recommended_products = [(recommendation.iid, recommendation.est) for recommendation in top_n_recommendations]
        return recommended_products

# Streamlit app
def main():
    st.title("Product Recommendation App")

    # User input for customer ID
    user_id_input = st.number_input("Enter customer ID:", min_value=int(df['customer_id'].min()), max_value=int(df['customer_id'].max()))

    # User input for top N recommendations
    top_n_input = st.number_input("Enter the number of recommendations (top N):", min_value=1, value=5)

    # Get recommendations when the user clicks the "Get Recommendations" button
    if st.button("Get Recommendations"):
        recommendations = get_top_n_recommendations(loaded_svd_model, user_id_input, n=top_n_input)
        
        # Display the recommendations
        if recommendations:
            st.success(f"Top {top_n_input} recommended products for customer with ID {user_id_input}:")
            for product_id, estimated_rating in recommendations:
                st.write(f"Product ID: {product_id}, Estimated Rating: {estimated_rating}")

    # Visualizations
    st.sidebar.title("Choose Visualization")
    visualization_option = st.sidebar.selectbox("Select visualization:", ["None", "Average Rating per Category", "Average Price per Category", "Purchases in Each Category", "Daily Purchases"])

    if visualization_option != "None":
        # Check if 'category' column exists in the DataFrame
        if 'category' in df.columns:
            if visualization_option == "Average Rating per Category" and 'ratings' in df.columns:
                # Average rating per category
                avg_rating_per_category = df.groupby('category')['ratings'].mean().reset_index()
                st.write("Average Rating per Category:")
                st.bar_chart(avg_rating_per_category.set_index('category'))

            elif visualization_option == "Average Price per Category" and 'price' in df.columns:
                # Average price per category
                avg_price_per_category = df.groupby('category')['price'].mean().reset_index()
                st.write("Average Price per Category:")
                st.bar_chart(avg_price_per_category.set_index('category'))

            elif visualization_option == "Purchases in Each Category":
                # Bar chart for purchases in each category
                category_purchase_counts = df['category'].value_counts().reset_index()
                category_purchase_counts.columns = ['Category', 'Number of Purchases']
                st.write("Purchases in Each Category:")
                st.bar_chart(category_purchase_counts.set_index('Category'))

            elif visualization_option == "Daily Purchases":
                # Line chart for daily purchases
                df['purchase_date'] = pd.to_datetime(df['purchase_date'])
                daily_purchases = df.groupby(df['purchase_date'].dt.date)['product_id'].count().reset_index()
                daily_purchases.columns = ['Date', 'Number of Purchases']
                st.write("Daily Purchases:")
                st.line_chart(daily_purchases.set_index('Date'))

    # Feedback comment
    st.sidebar.title("Feedback")
    feedback_comment = st.sidebar.text_area("Please leave your feedback here:")

    if st.sidebar.button("Submit Feedback"):
        st.sidebar.success("Thank you for your feedback!")

if __name__ == '__main__':
    main()
